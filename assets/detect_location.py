import streamlit as st

def render_location_bar(location_status, location_name):
    st.markdown("""
    <style>
        .location-card {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 0.75rem;
            max-width: 32rem;
            margin: 1rem auto;
        }

        .location-icon {
            width: 32px;
            height: 32px;
            border-radius: 0.5rem;
            background: rgba(46,125,50,0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            color: #2E7D32;
        }

        .location-label {
            font-size: 12px;
            color: #6b7280;
            margin: 0;
        }

        .location-value {
            font-size: 14px;
            font-weight: 500;
            margin: 0;
            color: #111827;
        }

        .location-warning {
            font-size: 11px;
            color: #dc2626;
            margin-top: 2px;
        }

        .spinner {
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
    </style>
    """, unsafe_allow_html=True)

    # Icon logic
    if location_status == "loading":
        icon = '<span class="spinner">⏳</span>'
        value = "Detecting your location..."
        warning = ""
    elif location_status == "denied":
        icon = "📍"
        value = location_name
        warning = '<p class="location-warning">Location access denied. Using default.</p>'
    else:
        icon = "📍"
        value = location_name
        warning = ""

    st.markdown(f"""
    <div class="location-card">
        <div class="location-icon">{icon}</div>
        <div>
            <p class="location-label">Detected Location</p>
            <p class="location-value">{value}</p>
            {warning}
        </div>
    </div>
    """, unsafe_allow_html=True)
