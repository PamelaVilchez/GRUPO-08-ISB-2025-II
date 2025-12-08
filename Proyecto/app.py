import streamlit as st
import numpy as np
import mne
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="BCI P300 Viewer", layout="wide")

st.title("BCI P300 Viewer")

# === Subir archivo EDF ===
uploaded = st.file_uploader("Cargar archivo EDF", type=["edf"])

if uploaded:
    st.success("Archivo cargado correctamente")

    # Guardar archivo temporal
    temp_path = "temp_uploaded.edf"
    with open(temp_path, "wb") as f:
        f.write(uploaded.getbuffer())

    st.write("Cargando archivo...")
    raw = mne.io.read_raw_edf(temp_path, preload=True)
    st.write(raw)

    # Mostrar canales
    st.subheader("Canales disponibles:")
    st.json({i: ch for i, ch in enumerate(raw.ch_names)})

    # Solo canales EEG
    eeg_chs = [ch for ch in raw.ch_names if ch.startswith("EEG_")]
    raw_eeg = raw.copy().pick(eeg_chs)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Señales EEG", "Eventos", "ERP", "P300 y Letra Detectada"])

    # ================================
    # TAB 1: Señales EEG
    # ================================
    with tab1:
        st.subheader("Mostrando señales EEG")
        fig1 = raw_eeg.plot(n_channels=10, duration=10, show=False, scalings=dict(eeg=40e-6))
        st.pyplot(fig1)

    # ================================
    # Extraer StimulusCode
    # ================================
    stim = raw.copy().pick(["StimulusCode"])[0][0][0]

    events = []
    for i in range(1, len(stim)):
        if stim[i] != 0 and stim[i - 1] == 0:
            events.append([i, 0, int(stim[i])])

    events = np.array(events, dtype=int)

    # Diccionario de eventos
    event_id = {
        "row_1": 1, "row_2": 2, "row_3": 3,
        "row_4": 4, "row_5": 5, "row_6": 6,
        "col_1": 7, "col_2": 8, "col_3": 9,
        "col_4": 10, "col_5": 11, "col_6": 12,
    }

    # Crear Epochs
    tmin = -0.1
    tmax = 0.8

    epochs = mne.Epochs(
        raw_eeg,
        events,
        event_id=event_id,
        tmin=tmin,
        tmax=tmax,
        baseline=(None, 0),
        preload=True
    )

    # ================================
    # TAB 2: Eventos
    # ================================
    with tab2:
        st.subheader("Eventos detectados (primeros 20):")
        st.write(events[:20])
        st.write(epochs)

    # ================================
    # TAB 3: ERP
    # ================================
    with tab3:
        st.subheader("Comparación ERP (Cz)")

        evokeds = {cond: epochs[cond].average() for cond in epochs.event_id.keys()}

        colors = plt.cm.tab20.colors
        colors = {cond: colors[i] for i, cond in enumerate(evokeds.keys())}

        fig_list = mne.viz.plot_compare_evokeds(
            evokeds,
            picks="EEG_Cz",
            colors=colors,
            legend="upper right",
            show=False
        )

        fig2 = fig_list[0]
        st.pyplot(fig2)

    # ================================
    # TAB 4: P300 + LETRA DETECTADA
    # ================================
    with tab4:
        st.subheader("Cálculo de amplitud P300 en Cz")

        p300_window = (0.3, 0.6)
        sfreq = raw.info["sfreq"]

        start_idx = int((p300_window[0] - tmin) * sfreq)
        end_idx = int((p300_window[1] - tmin) * sfreq)

        p300_amplitudes = {}

        for cond, evk in evokeds.items():
            signal_cz = evk.data[evk.ch_names.index("EEG_Cz")]
            p300_peak = np.max(signal_cz[start_idx:end_idx])
            p300_amplitudes[cond] = p300_peak

        st.write("### Amplitudes P300 (µV)")
        for cond, amp in p300_amplitudes.items():
            st.write(f"**{cond}: {amp*1e6:.2f} µV**")

        # =====================================
        # Detección de fila y columna ganadora
        # =====================================
        row_values = {k: v for k, v in p300_amplitudes.items() if "row" in k}
        col_values = {k: v for k, v in p300_amplitudes.items() if "col" in k}

        detected_row = max(row_values, key=row_values.get)
        detected_col = max(col_values, key=col_values.get)

        row_index = int(detected_row.split("_")[1]) - 1
        col_index = int(detected_col.split("_")[1]) - 1

        # ============================
        # MATRIZ 6x6 DEL P300 SPELLER
        # ============================
        matrix_6x6 = [
            ["A","B","C","D","E","F"],
            ["G","H","I","J","K","L"],
            ["M","N","O","P","Q","R"],
            ["S","T","U","V","W","X"],
            ["Y","Z","1","2","3","4"],
            ["5","6","7","8","9","0"]
        ]

        detected_letter = matrix_6x6[row_index][col_index]

        st.success(f"### Letra detectada: **{detected_letter}**")
        st.write(f"Fila detectada: **{detected_row}**")
        st.write(f"Columna detectada: **{detected_col}**")
