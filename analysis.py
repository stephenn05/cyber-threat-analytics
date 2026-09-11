import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Путь к данным
DATA_PATH = Path("data/incidents.csv")

# Загрузка данных
df = pd.read_csv(DATA_PATH)

print("=== ОБЩАЯ ИНФОРМАЦИЯ ===")
print(f"Всего инцидентов: {len(df)}")
print(f"Количество типов угроз: {df['threat_type'].nunique()}")
print(f"Средний уровень риска: {df['risk_score'].mean():.2f}")

print("\n=== РАСПРЕДЕЛЕНИЕ ПО ТИПАМ УГРОЗ ===")
threat_counts = df["threat_type"].value_counts()
print(threat_counts)

print("\n=== РАСПРЕДЕЛЕНИЕ ПО КРИТИЧНОСТИ ===")
severity_counts = df["severity"].value_counts()
print(severity_counts)

print("\n=== СРЕДНИЙ РИСК ПО ТИПАМ УГРОЗ ===")
risk_by_threat = df.groupby("threat_type")["risk_score"].mean().sort_values(ascending=False)
print(risk_by_threat.round(2))

print("\n=== АНАЛИТИЧЕСКИЕ ВЫВОДЫ ===")
most_common_threat = threat_counts.idxmax()
highest_risk_threat = risk_by_threat.idxmax()

print(f"Наиболее распространённый тип угрозы: {most_common_threat}")
print(f"Наиболее высокий средний риск: {highest_risk_threat}")

# Создание папки для результатов
Path("results").mkdir(exist_ok=True)

# График 1: типы угроз
plt.figure(figsize=(10, 5))
threat_counts.plot(kind="bar")
plt.title("Распределение киберинцидентов по типам угроз")
plt.xlabel("Тип угрозы")
plt.ylabel("Количество инцидентов")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("results/threat_types.png")
plt.close()

# График 2: критичность
plt.figure(figsize=(8, 5))
severity_counts.plot(kind="bar")
plt.title("Распределение инцидентов по критичности")
plt.xlabel("Уровень критичности")
plt.ylabel("Количество инцидентов")
plt.tight_layout()
plt.savefig("results/severity.png")
plt.close()

print("\nГрафики сохранены в папку results/")
