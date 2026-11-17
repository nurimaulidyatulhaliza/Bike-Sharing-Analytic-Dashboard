
import os
import base64
import pandas as pd
import plotly.express as px
import streamlit as st



COLORS = {
    "purple": "#E8DFF5",
    "blue": "#DCEAF7",
    "green": "#DDEBDD",
}

BACKGROUND = "#FFFFFF"
TEXT_COLOR = "#404040"
GRID_COLOR = "#EAEAEA"

STROKE = {
    "purple": "#A994D1",
    "blue": "#7FA9D6",
    "green": "#8DBB8D",
}



IMAGE_PATH = r"proyek_analisis_data\Bike Sharing.jpg"

if os.path.exists(IMAGE_PATH):
    with open(IMAGE_PATH, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode("utf-8")
else:
    encoded_image = None


st.set_page_config(
    page_title="Bike Sharing Analytics Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)

header_background = (
    f'url("data:image/jpeg;base64,{encoded_image}")'
    if encoded_image
    else COLORS["purple"]
)

css = f"""
<style>

    .stApp {{
        background-color: {BACKGROUND};
        color: {TEXT_COLOR};
    }}

    h1, h2, h3, h4, p, label, span, li {{
        color: {TEXT_COLOR};
    }}

    /* SIDEBAR */

    section[data-testid="stSidebar"] {{
        background: linear-gradient(
            180deg,
            {COLORS["purple"]} 0%,
            {COLORS["blue"]} 100%
        );
    }}

    section[data-testid="stSidebar"] * {{
        color: {TEXT_COLOR} !important;
    }}

    /* HEADER WITH IMAGE */

    .main-header {{
        background:
            linear-gradient(
                rgba(30, 30, 30, 0.40),
                rgba(30, 30, 30, 0.40)
            ),
            {header_background};

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;

        padding: 55px 35px;
        border-radius: 20px;
        margin-bottom: 22px;
        min-height: 200px;

        display: flex;
        flex-direction: column;
        justify-content: center;

        box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    }}

    .main-header h1 {{
        margin: 0;
        font-size: 2rem;
        color: white !important;
    }}

    .main-header p {{
        margin: 8px 0 0 0;
        font-size: 1rem;
        color: white !important;
    }}

    /* KPI CARDS */

    .kpi-card {{
        padding: 18px 20px;
        border-radius: 18px;
        height: 100%;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        transition: transform .2s ease, box-shadow .2s ease;
    }}

    .kpi-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 18px rgba(0,0,0,0.09);
    }}

    .kpi-label {{
        font-size: .85rem;
        font-weight: 600;
        opacity: .8;
    }}

    .kpi-value {{
        font-size: 1.8rem;
        font-weight: 700;
        margin: 4px 0;
    }}

    .kpi-sub {{
        font-size: .8rem;
        opacity: .75;
    }}

    /* INSIGHT */

    .insight {{
        padding: 14px 18px;
        border-radius: 14px;
        margin-top: 14px;
        border-left: 6px solid;
        font-size: .95rem;
        line-height: 1.55;
    }}

    /* TABS */

    button[data-baseweb="tab"] {{
        background-color: {GRID_COLOR};
        border-radius: 12px 12px 0 0;
        padding: 10px 18px;
        margin-right: 6px;
        font-weight: 600;
    }}

    button[data-baseweb="tab"][aria-selected="true"] {{
        background-color: {COLORS["purple"]};
    }}

    div[data-baseweb="tab-highlight"] {{
        background-color: {STROKE["purple"]} !important;
    }}

    /* EXPANDER */

    div[data-testid="stExpander"] {{
        background-color: white;
        border-radius: 14px;
        border: 1px solid {GRID_COLOR};
    }}

    /* FOOTER */

    .footer {{
        text-align: center;
        color: #9a9a9a;
        font-size: .8rem;
        padding: 10px 0;
    }}

</style>
"""

st.markdown(css, unsafe_allow_html=True)


def kpi_card(label, value, sub, color):
    return f"""
    <div class="kpi-card" style="background:{COLORS[color]};">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>
    """


def insight(text, color="green", stroke="green"):
    st.markdown(
        f"""
        <div class="insight"
             style="background:{COLORS[color]};
                    border-color:{STROKE[stroke]};">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def style_fig(fig, height=430):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="white",
        font=dict(color=TEXT_COLOR, family="Inter, sans-serif"),
        margin=dict(l=10, r=10, t=50, b=10),
        hovermode="x unified",
        legend=dict(
            title="",
            orientation="h",
            y=1.12,
            x=0,
        ),
        title_font=dict(size=16),
    )

    fig.update_xaxes(
        gridcolor=GRID_COLOR,
        linecolor=GRID_COLOR,
    )

    fig.update_yaxes(
        gridcolor=GRID_COLOR,
        linecolor=GRID_COLOR,
    )

    return fig


@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    day_df = pd.read_csv(
        os.path.join(current_dir, "main_day_data.csv")
    )

    hour_df = pd.read_csv(
        os.path.join(current_dir, "main_hour_data.csv")
    )

    day_df["dateday"] = pd.to_datetime(day_df["dateday"])
    hour_df["dateday"] = pd.to_datetime(hour_df["dateday"])

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    day_df["month"] = pd.Categorical(
        day_df["month"],
        categories=month_order,
        ordered=True,
    )

    return day_df, hour_df, month_order


day_df, hour_df, month_order = load_data()


with st.sidebar:
    st.markdown("## 🚲 Bike Sharing Control")

    st.caption(
        "Atur filter untuk mengeksplorasi data secara dinamis."
    )

    st.markdown("---")

    min_date = day_df["dateday"].min().date()
    max_date = day_df["dateday"].max().date()

    date_range = st.date_input(
        "📅 Rentang Tanggal",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
    )

    all_seasons = day_df["season"].unique().tolist()

    selected_seasons = st.multiselect(
        "🍂 Musim",
        all_seasons,
        default=all_seasons,
    )

    all_workingday = day_df["workingday"].unique().tolist()

    selected_workingday = st.multiselect(
        "💼 Tipe Hari",
        all_workingday,
        default=all_workingday,
    )

    st.markdown("---")

    st.info(
        "💡 Grafik dan KPI akan berubah otomatis mengikuti filter."
    )


if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range[0]


if not selected_seasons:
    selected_seasons = all_seasons

if not selected_workingday:
    selected_workingday = all_workingday


main_day_df = day_df[
    (day_df["dateday"].dt.date >= start_date)
    & (day_df["dateday"].dt.date <= end_date)
    & (day_df["season"].isin(selected_seasons))
    & (day_df["workingday"].isin(selected_workingday))
]


main_hour_df = hour_df[
    (hour_df["dateday"].dt.date >= start_date)
    & (hour_df["dateday"].dt.date <= end_date)
    & (hour_df["season"].isin(selected_seasons))
    & (hour_df["workingday"].isin(selected_workingday))
]


st.markdown(
    """
    <div class="main-header">
        <h1>🚲 Bike Sharing Analytics Dashboard (2011–2012)</h1>
        <p>
            Eksplorasi interaktif pola mobilitas pelanggan,
            pengaruh musim & cuaca, serta tren pertumbuhan bisnis.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


if main_day_df.empty:
    st.warning(
        "Tidak ada data untuk kombinasi filter ini. "
        "Coba ubah filter di sidebar."
    )
    st.stop()


total_rentals = int(main_day_df["total_count"].sum())
total_registered = int(main_day_df["registered"].sum())
total_casual = int(main_day_df["casual"].sum())

pct_reg = (
    total_registered / total_rentals * 100
    if total_rentals else 0
)

pct_cas = (
    total_casual / total_rentals * 100
    if total_rentals else 0
)

avg_daily = int(main_day_df["total_count"].mean())


c1, c2, c3, c4 = st.columns(4)

c1.markdown(
    kpi_card(
        "Total Penyewaan",
        f"{total_rentals:,}",
        f"{len(main_day_df):,} hari terpilih",
        "blue",
    ),
    unsafe_allow_html=True,
)

c2.markdown(
    kpi_card(
        "Pengguna Registered",
        f"{total_registered:,}",
        f"{pct_reg:.1f}% dari total",
        "green",
    ),
    unsafe_allow_html=True,
)

c3.markdown(
    kpi_card(
        "Pengguna Casual",
        f"{total_casual:,}",
        f"{pct_cas:.1f}% dari total",
        "purple",
    ),
    unsafe_allow_html=True,
)

c4.markdown(
    kpi_card(
        "Rata-rata Harian",
        f"{avg_daily:,}",
        "sepeda / hari",
        "blue",
    ),
    unsafe_allow_html=True,
)


st.markdown("<br>", unsafe_allow_html=True)


tab1, tab2, tab3, tab4 = st.tabs(
    [
        "⏰ Pola Jam Sibuk",
        "🌦️ Musim & Cuaca",
        "📈 Tren Pertumbuhan",
        "🎯 Klasterisasi Suhu",
    ]
)


with tab1:

    st.subheader(
        "Aktivitas Penyewaan per Jam: Hari Kerja vs Hari Libur"
    )

    hourly = (
        main_hour_df
        .groupby(["workingday", "hour"])[
            ["registered", "casual"]
        ]
        .mean()
        .reset_index()
        .melt(
            id_vars=["workingday", "hour"],
            var_name="Tipe",
            value_name="Rata-rata",
        )
    )

    hourly["Tipe"] = hourly["Tipe"].map(
        {
            "registered": "Registered (Member)",
            "casual": "Casual (Biasa)",
        }
    )

    if hourly.empty:

        st.info("Data per jam kosong untuk filter ini.")

    else:

        fig1 = px.line(
            hourly,
            x="hour",
            y="Rata-rata",
            color="Tipe",
            facet_col="workingday",
            markers=True,
            color_discrete_map={
                "Registered (Member)": STROKE["blue"],
                "Casual (Biasa)": STROKE["purple"],
            },
            labels={
                "hour": "Jam",
                "workingday": "",
            },
        )

        fig1.update_traces(
            line=dict(width=3),
            marker=dict(size=7),
        )

        fig1.update_xaxes(dtick=2)

        fig1.for_each_annotation(
            lambda a: a.update(
                text=a.text.split("=")[-1]
            )
        )

        st.plotly_chart(
            style_fig(fig1),
            use_container_width=True,
        )

    insight(
        "📌 <b>Key Insight:</b> Pada <b>Hari Kerja</b> terjadi dua "
        "lonjakan (<i>commuter rush</i>) pukul <b>08.00</b> dan "
        "<b>17.00–18.00</b> yang didominasi pengguna "
        "<i>Registered</i>. Pada <b>Hari Libur</b>, penyewaan naik "
        "santai di siang hari (<b>12.00–16.00</b>) untuk rekreasi.",
        "green",
        "green",
    )


with tab2:

    st.subheader(
        "Dampak Musim dan Cuaca terhadap Penyewaan Harian"
    )

    pastel_seq = [
        COLORS["purple"],
        COLORS["blue"],
        COLORS["green"],
    ]

    stroke_seq = [
        STROKE["purple"],
        STROKE["blue"],
        STROKE["green"],
    ]

    col_a, col_b = st.columns(2)

    with col_a:

        season_avg = (
            main_day_df
            .groupby("season")["total_count"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig_s = px.bar(
            season_avg,
            x="season",
            y="total_count",
            color="season",
            text_auto=",.0f",
            color_discrete_sequence=pastel_seq,
            labels={
                "season": "Musim",
                "total_count": "Rata-rata / Hari",
            },
            title="Rata-rata Penyewaan per Musim",
        )

        fig_s.update_traces(
            marker_line_width=2,
            textposition="outside",
            cliponaxis=False,
        )

        for i, tr in enumerate(fig_s.data):
            tr.marker.line.color = stroke_seq[
                i % len(stroke_seq)
            ]

        fig_s.update_layout(
            showlegend=False,
            hovermode="closest",
        )

        st.plotly_chart(
            style_fig(fig_s, 400),
            use_container_width=True,
        )

    with col_b:

        weather_avg = (
            main_day_df
            .groupby("weathersit")["total_count"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig_w = px.bar(
            weather_avg,
            x="weathersit",
            y="total_count",
            color="weathersit",
            text_auto=",.0f",
            color_discrete_sequence=[
                COLORS["green"],
                COLORS["blue"],
                COLORS["purple"],
            ],
            labels={
                "weathersit": "Kondisi Cuaca",
                "total_count": "Rata-rata / Hari",
            },
            title="Rata-rata Penyewaan per Cuaca",
        )

        fig_w.update_traces(
            marker_line_width=2,
            textposition="outside",
            cliponaxis=False,
        )

        edge = [
            STROKE["green"],
            STROKE["blue"],
            STROKE["purple"],
        ]

        for i, tr in enumerate(fig_w.data):
            tr.marker.line.color = edge[
                i % len(edge)
            ]

        fig_w.update_layout(
            showlegend=False,
            hovermode="closest",
        )

        st.plotly_chart(
            style_fig(fig_w, 400),
            use_container_width=True,
        )

    insight(
        "🌦️ <b>Key Insight:</b> <b>Musim Gugur (Fall)</b> mencatat "
        "permintaan tertinggi, sedangkan <b>Musim Semi (Spring)</b> "
        "terendah. Cuaca cerah menghasilkan hampir <b>3 kali lipat</b> "
        "penyewaan dibandingkan hujan ringan/salju.",
        "blue",
        "blue",
    )


with tab3:

    st.subheader(
        "Perbandingan Performa Penyewaan Bulanan (2011 vs 2012)"
    )

    monthly = (
        main_day_df
        .groupby(
            ["year", "month"],
            observed=False,
        )["total_count"]
        .sum()
        .reset_index()
    )

    monthly = monthly[
        monthly["total_count"] > 0
    ]

    monthly["year"] = monthly["year"].astype(str)

    fig3 = px.line(
        monthly,
        x="month",
        y="total_count",
        color="year",
        markers=True,
        category_orders={
            "month": month_order,
        },
        color_discrete_map={
            "2011": STROKE["purple"],
            "2012": STROKE["blue"],
        },
        labels={
            "month": "Bulan",
            "total_count": "Total Penyewaan",
            "year": "Tahun",
        },
    )

    fig3.update_traces(
        line=dict(width=3.5),
        marker=dict(size=9),
    )

    st.plotly_chart(
        style_fig(fig3, 450),
        use_container_width=True,
    )

    insight(
        "📈 <b>Key Insight:</b> Bisnis tumbuh konsisten sepanjang "
        "<b>2012</b> dibandingkan <b>2011</b> di setiap bulan, "
        "dengan puncak volume pada kuartal ketiga "
        "(<b>Juli – September</b>).",
        "purple",
        "purple",
    )


with tab4:

    st.subheader(
        "Klasterisasi Permintaan Berdasarkan Kategori Suhu"
    )

    temp_df = main_day_df.copy()

    temp_df["Kategori Suhu"] = pd.cut(
        temp_df["temp"],
        bins=[0, 15, 25, 45],
        labels=[
            "Sejuk (<15°C)",
            "Nyaman (15–25°C)",
            "Hangat/Panas (>25°C)",
        ],
    )

    cluster = (
        temp_df
        .groupby(
            "Kategori Suhu",
            observed=False,
        )
        .agg(
            Jumlah_Hari=("total_count", "count"),
            Rata_Rata_Sewa=("total_count", "mean"),
            Total_Sewa=("total_count", "sum"),
        )
        .reset_index()
    )

    left, right = st.columns([1.4, 1])

    with left:

        fig4 = px.bar(
            cluster,
            x="Kategori Suhu",
            y="Rata_Rata_Sewa",
            color="Kategori Suhu",
            text_auto=",.0f",
            color_discrete_sequence=[
                COLORS["blue"],
                COLORS["green"],
                COLORS["purple"],
            ],
            labels={
                "Rata_Rata_Sewa": "Rata-rata Penyewaan / Hari",
            },
            title="Rata-rata Penyewaan per Klaster Suhu",
        )

        fig4.update_traces(
            marker_line_width=2,
            textposition="outside",
            cliponaxis=False,
        )

        for tr, c in zip(
            fig4.data,
            [
                STROKE["blue"],
                STROKE["green"],
                STROKE["purple"],
            ],
        ):
            tr.marker.line.color = c

        fig4.update_layout(
            showlegend=False,
            hovermode="closest",
        )

        st.plotly_chart(
            style_fig(fig4, 400),
            use_container_width=True,
        )

    with right:

        st.markdown("#### 📋 Ringkasan Segmen Suhu")

        st.dataframe(
            cluster.style.format(
                {
                    "Rata_Rata_Sewa": "{:,.0f}",
                    "Total_Sewa": "{:,.0f}",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

        st.caption(
            "Klasterisasi berbasis aturan (binning) membantu tim "
            "operasional menyiapkan stok sepeda saat suhu nyaman "
            "hingga hangat."
        )


st.markdown("<br>", unsafe_allow_html=True)

with st.expander("🔍 Lihat & Unduh Data Hasil Filter"):

    st.dataframe(
        main_day_df.head(50),
        use_container_width=True,
    )

    st.download_button(
        "⬇️ Unduh CSV (hasil filter)",
        main_day_df.to_csv(index=False).encode("utf-8"),
        file_name="bike_sharing_filtered.csv",
        mime="text/csv",
    )
