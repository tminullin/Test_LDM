import os

BASE_DIR = "Docs"

# Описание структуры: {путь к файлу: заголовок в SUMMARY.md}
structure = {
    "01-project-overview/01-goals.md": "1.1 Цели",
    "01-project-overview/02-tasks.md": "1.2 Роли пользователей",
    "01-project-overview/03-scope.md": "1.3 Возможности системы",
    "01-project-overview/04-users.md": "1.4 Роли пользователей, сценарии, проблемы и цели",
    "01-project-overview/05-stakeholders.md": "1.5 Стейкхолдеры",
    "01-project-overview/06-monitoring.md": "1.6 Монитоирнг и логирование",
    "01-project-overview/07-data-protection.md": "1.7 Безопасность данных",

    "02-user-stories/01-med-docs.md": "2.1 Управление документацией",
    "02-user-stories/02-security.md": "2.2 Управление доступом и безопасностью",
    "02-user-stories/03-integrations.md": "2.3 Интеграции и обмен данными",
    "02-user-stories/04-scalability.md": "2.4 Масштабирование и производительность",

    "03-architecture/01-overview.md": "3.1 Общая схема",

    "04-database/01-db-model.md": "4.1 Модель данных",

    "05-integration/01-restapi.md": "5.1 Интеграция REST",
    "05-integration/02-async.md": "5.2 Асинхронная интеграция",
    "05-integration/03-flow.md": "5.3 Диаграмма",

    "06-data-security/01-data-security.md": "6.1 Безопасность данных",
}

# Создание директорий и файлов
for path, title in structure.items():
    full_path = os.path.join(BASE_DIR, path)
    folder = os.path.dirname(full_path)
    os.makedirs(folder, exist_ok=True)
    if not os.path.exists(full_path):
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n")

# Формирование SUMMARY.md
summary_lines = [
    "# Summary\n",
    "## 1. Основная информация",
    f"- [{structure['01-project-overview/01-goals.md']}](01-project-overview/01-goals.md)",
    f"- [{structure['01-project-overview/02-tasks.md']}](01-project-overview/02-tasks.md)",
    f"- [{structure['01-project-overview/03-scope.md']}](01-project-overview/03-scope.md)",
    f"- [{structure['01-project-overview/04-users.md']}](01-project-overview/04-users.md)",
    f"- [{structure['01-project-overview/05-stakeholders.md']}](01-project-overview/05-stakeholders.md)",
    f"- [{structure['01-project-overview/06-monitoring.md']}](01-project-overview/06-monitoring.md)",
    f"- [{structure['01-project-overview/07-data-protection.md']}](01-project-overview/07-data-protection.md)",

    "## 2. Пользовательские истории",
    f"- [{structure['02-user-stories/01-med-docs.md']}](02-user-stories/01-med-docs.md)",
    f"- [{structure['02-user-stories/02-security.md']}](02-user-stories/02-security.md)",
    f"- [{structure['02-user-stories/03-integrations.md']}](02-user-stories/03-integrations.md)",
    f"- [{structure['02-user-stories/04-scalability.md']}](02-user-stories/04-scalability.md)",

    "## 3. Описание архитектуры",
    f"- [{structure['03-architecture/01-overview.md']}](03-architecture/01-overview.md)",

    "## 4. Описание слоя хранения",
    f"- [{structure['04-database/01-db-model.md']}](04-database/01-db-model.md)",

    "## 5. Описание интеграционного профиля",
    f"- [{structure['05-integration/01-restapi.md']}](05-integration/01-restapi.md)",
    f"- [{structure['05-integration/02-async.md']}](05-integration/02-async.md)",
    f"- [{structure['05-integration/03-flow.md']}](05-integration/03-flow.md)",

    "## 6. Описание безопасности данных",
    f"- [{structure['06-data-security/01-data-security.md']}](06-data-security/01-data-security.md)",
]

summary_path = os.path.join(BASE_DIR, "SUMMARY.md")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write("\n".join(summary_lines))

print("✅ Папка Docs со структурой и SUMMARY.md создана")
