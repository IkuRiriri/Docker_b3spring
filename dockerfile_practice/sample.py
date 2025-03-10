import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

# マジックナンバーの定義
CSV_FILES = ['data/2units.csv','data/3units.csv', 'data/4units.csv', 'data/5units.csv']  # CSVファイルパスのリスト
LEGEND_LABELS = ['2 Units', '3 Units', '4 Units', '5 Units']  # 凡例のラベル
LINE_STYLES = {
    '2 Units': {'color': '#FF0000', 'linestyle': '-', 'linewidth': 2},    # 赤色、実線
    '3 Units': {'color': '#0000FF', 'linestyle': '-', 'linewidth': 2},    # 青色、実線
    '4 Units': {'color': '#00FF00', 'linestyle': '-', 'linewidth': 2},    # 緑色、実線
    '5 Units': {'color': '#000000', 'linestyle': '-', 'linewidth': 2}     # 黒色、実線
}
TIME_RANGE = {
    'min': 0,
    'max': 10000  # ミリ秒単位での最大値
}
TIME_STEP = 1  # サンプリング間隔（ミリ秒）

def load_csv_files(file_paths: List[str]) -> Dict[str, pd.DataFrame]:
    """CSVファイルを読み込み、DataFrameとして返す"""
    dataframes = {}
    for file_path in file_paths:
        try:
            df = pd.read_csv(file_path)
            dataframes[file_path] = df
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    return dataframes

def calculate_solution_progress(df: pd.DataFrame, time_points: list) -> pd.DataFrame:
    """各時点でのFirst/Final Solution達成率を計算"""
    total_count = len(df)
    progress_data = []

    for time in time_points:
        first_count = len(df[df['First_Solution_Time'] <= time])
        final_count = len(df[df['Final_Solution_Time'] <= time])

        progress_data.append({
            'Time': time,
            'First_Progress': (first_count / total_count) * 100,
            'Final_Progress': (final_count / total_count) * 100
        })

    return pd.DataFrame(progress_data)

def calculate_solution_type_distribution(df: pd.DataFrame) -> pd.Series:
    """Solution_Typeの分布を計算"""
    return (df['Solution_Type'].value_counts() / len(df) * 100).round(2)

def plot_solution_progress(dataframes: Dict[str, pd.DataFrame], time_points: list, output_path_prefix: str):
    """解決時間の進行をプロット"""
    # データの準備
    plot_data = []
    for (file_name, df), legend_label in zip(dataframes.items(), LEGEND_LABELS):
        progress_df = calculate_solution_progress(df, time_points)
        # ミリ秒から秒への変換
        progress_df['Time'] = progress_df['Time'] / 1000.0

        # First Solution データ
        first_data = progress_df[['Time', 'First_Progress']].copy()
        first_data['File'] = legend_label
        first_data['Type'] = 'First'
        first_data = first_data.rename(columns={'First_Progress': 'Progress'})

        # Final Solution データ
        final_data = progress_df[['Time', 'Final_Progress']].copy()
        final_data['File'] = legend_label
        final_data['Type'] = 'Final'
        final_data = final_data.rename(columns={'Final_Progress': 'Progress'})

        plot_data.extend([first_data, final_data])

    # データを結合
    plot_df = pd.concat(plot_data, ignore_index=True)

    # Matplotlib & Seabornの設定
    import matplotlib.pyplot as plt

    # グリッドスタイルを直接設定
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.alpha'] = 0.5

    # First Solution のプロット
    fig1, ax1 = plt.subplots(figsize=(12, 5))
    first_data = plot_df[plot_df['Type'] == 'First']

    # 各ケースを個別にプロット
    for label in LEGEND_LABELS:
        case_data = first_data[first_data['File'] == label]
        ax1.plot(case_data['Time'], case_data['Progress'],
                label=label,
                **LINE_STYLES[label])

    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Solutions Found (%)')
    ax1.set_title('First Solution Progress')
    ax1.set_xlim(TIME_RANGE['min']/1000, TIME_RANGE['max']/1000)
    # 凡例を右下に配置
    ax1.legend(bbox_to_anchor=(1.02, 0.1), loc='lower left')
    plt.tight_layout()
    plt.savefig(f'{output_path_prefix}_first.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Final Solution のプロット
    fig2, ax2 = plt.subplots(figsize=(12, 5))
    final_data = plot_df[plot_df['Type'] == 'Final']

    # 各ケースを個別にプロット
    for label in LEGEND_LABELS:
        case_data = final_data[final_data['File'] == label]
        ax2.plot(case_data['Time'], case_data['Progress'],
                label=label,
                **LINE_STYLES[label])

    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Solutions Found (%)')
    ax2.set_title('Optimal Solution Progress')
    ax2.set_xlim(TIME_RANGE['min']/1000, TIME_RANGE['max']/1000)
    # 凡例を右下に配置
    ax2.legend(bbox_to_anchor=(1.02, 0.1), loc='lower left')
    plt.tight_layout()
    plt.savefig(f'{output_path_prefix}_final.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_solution_type_table(dataframes: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Solution_Type分布のテーブルを作成"""
    distributions = {}

    for file_name, df in dataframes.items():
        distributions[file_name] = calculate_solution_type_distribution(df)

    # 全てのSolution_Typeを含むテーブルを作成
    distribution_df = pd.DataFrame(distributions).T
    distribution_df = distribution_df.fillna(0.0)  # 欠損値を0%で埋める

    return distribution_df

def main():
    # 時間点の生成
    time_points = list(range(TIME_RANGE['min'], TIME_RANGE['max'] + TIME_STEP, TIME_STEP))

    # CSVファイルの読み込み
    dataframes = load_csv_files(CSV_FILES)
    if not dataframes:
        print("No valid CSV files found.")
        return

    # 解決時間進行グラフの生成
    plot_solution_progress(dataframes, time_points, 'output/solution_progress')


if __name__ == "__main__":
    main()