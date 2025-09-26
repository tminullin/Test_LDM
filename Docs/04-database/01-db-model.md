# 4.1 Модель данных

## Физическая модель базы данных&#x20;

#### Таблица `Employees`

| Поле             | Тип данных   | Ограничения                 | Описание                    |
| ---------------- | ------------ | --------------------------- | --------------------------- |
| `EmployeeID`     | SERIAL       | PK                          | Первичный ключ сотрудника   |
| `FullName`       | VARCHAR(255) | NOT NULL                    | Полное имя сотрудника       |
| `Position`       | VARCHAR(100) |                             | Должность                   |
| `Specialization` | VARCHAR(100) |                             | Специализация               |
| `SNILS`          | VARCHAR(20)  | UNIQUE                      | СНИЛС (уникальный)          |
| `CreatedAt`      | TIMESTAMP    | DEFAULT CURRENT\_TIMESTAMP  | Время создания записи       |
| `UpdatedAt`      | TIMESTAMP    | DEFAULT CURRENT\_TIMESTAMP  | Время последнего обновления |
| `CreatedBy`      | INTEGER      | FK → `Employees.EmployeeID` | Кто создал запись           |

#### Таблица `UserProfiles`

| Поле         | Тип данных | Ограничения                 | Описание                    |
| ------------ | ---------- | --------------------------- | --------------------------- |
| `ProfileID`  | SERIAL     | PK                          | Первичный ключ профиля      |
| `EmployeeID` | INTEGER    | FK → `Employees.EmployeeID` | Ссылка на сотрудника        |
| `Settings`   | JSONB      |                             | Настройки пользователя      |
| `CreatedAt`  | TIMESTAMP  | DEFAULT CURRENT\_TIMESTAMP  | Время создания записи       |
| `UpdatedAt`  | TIMESTAMP  | DEFAULT CURRENT\_TIMESTAMP  | Время последнего обновления |
| `CreatedBy`  | INTEGER    | FK → `Employees.EmployeeID` | Кто создал запись           |

#### Таблица `Patients`

| Поле        | Тип данных   | Ограничения                   | Описание                    |
| ----------- | ------------ | ----------------------------- | --------------------------- |
| `PatientID` | SERIAL       | PK                            | Первичный ключ пациента     |
| `FullName`  | VARCHAR(255) | NOT NULL                      | Полное имя пациента         |
| `BirthDate` | DATE         |                               | Дата рождения               |
| `Gender`    | CHAR(1)      | CHECK (Gender IN ('M','F'))   | Пол (M/F)                   |
| `Contacts`  | VARCHAR(255) |                               | Контактная информация       |
| `SNILS`     | VARCHAR(20)  | UNIQUE                        | СНИЛС (уникальный)          |
| `PolicyOMS` | VARCHAR(20)  |                               | Полис ОМС                   |
| `AddressID` | INTEGER      | FK → `RefAddresses.AddressID` | Ссылка на адрес             |
| `CreatedAt` | TIMESTAMP    | DEFAULT CURRENT\_TIMESTAMP    | Время создания записи       |
| `UpdatedAt` | TIMESTAMP    | DEFAULT CURRENT\_TIMESTAMP    | Время последнего обновления |
| `CreatedBy` | INTEGER      | FK → `Employees.EmployeeID`   | Кто создал запись           |

#### Таблица `Documents`

| Поле             | Тип данных  | Ограничения                            | Описание                    |
| ---------------- | ----------- | -------------------------------------- | --------------------------- |
| `DocumentID`     | SERIAL      | PK                                     | Первичный ключ документа    |
| `PatientID`      | INTEGER     | FK → `Patients.PatientID`              | Ссылка на пациента          |
| `EmployeeID`     | INTEGER     | FK → `Employees.EmployeeID`            | Ссылка на сотрудника        |
| `DocumentTypeID` | INTEGER     | FK → `DocumentTypes.DocumentTypeID`    | Тип документа               |
| `OrganizationID` | INTEGER     | FK → `RefOrganizations.OrganizationID` | Ссылка на организацию       |
| `DiagnosisID`    | INTEGER     | FK → `RefDiseases.DiseaseID`           | Ссылка на диагноз           |
| `DrugID`         | INTEGER     | FK → `RefDrugs.DrugID`                 | Ссылка на препарат          |
| `ProfileMPID`    | INTEGER     | FK → `RefProfilesMP.ProfileID`         | Профиль медицинской помощи  |
| `Number`         | VARCHAR(50) |                                        | Номер документа             |
| `Date`           | DATE        |                                        | Дата документа              |
| `Content`        | TEXT        |                                        | Содержимое документа        |
| `Status`         | VARCHAR(50) |                                        | Статус документа            |
| `CreatedAt`      | TIMESTAMP   | DEFAULT CURRENT\_TIMESTAMP             | Время создания записи       |
| `UpdatedAt`      | TIMESTAMP   | DEFAULT CURRENT\_TIMESTAMP             | Время последнего обновления |
| `CreatedBy`      | INTEGER     | FK → `Employees.EmployeeID`            | Кто создал запись           |

#### Таблица `SEMD`

| Поле              | Тип данных  | Ограничения                     | Описание                    |
| ----------------- | ----------- | ------------------------------- | --------------------------- |
| `SEMDID`          | SERIAL      | PK                              | Первичный ключ СЭМД         |
| `DocumentID`      | INTEGER     | FK → `Documents.DocumentID`     | Ссылка на документ          |
| `TemplateID`      | INTEGER     | FK → `SEMDTemplates.TemplateID` | Ссылка на шаблон            |
| `SignatureStatus` | VARCHAR(50) |                                 | Статус подписи              |
| `CreatedAt`       | TIMESTAMP   | DEFAULT CURRENT\_TIMESTAMP      | Время создания записи       |
| `UpdatedAt`       | TIMESTAMP   | DEFAULT CURRENT\_TIMESTAMP      | Время последнего обновления |
| `CreatedBy`       | INTEGER     | FK → `Employees.EmployeeID`     | Кто создал запись           |

#### Таблица `DocumentTypes`

| Поле             | Тип данных   | Ограничения                 | Описание                      |
| ---------------- | ------------ | --------------------------- | ----------------------------- |
| `DocumentTypeID` | SERIAL       | PK                          | Первичный ключ типа документа |
| `Name`           | VARCHAR(100) |                             | Название типа документа       |
| `CreatedAt`      | TIMESTAMP    | DEFAULT CURRENT\_TIMESTAMP  | Время создания записи         |
| `UpdatedAt`      | TIMESTAMP    | DEFAULT CURRENT\_TIMESTAMP  | Время последнего обновления   |
| `CreatedBy`      | INTEGER      | FK → `Employees.EmployeeID` | Кто создал запись             |

#### Таблица `DocumentStructures`

| Поле             | Тип данных | Ограничения                         | Описание                       |
| ---------------- | ---------- | ----------------------------------- | ------------------------------ |
| `StructureID`    | SERIAL     | PK                                  | Первичный ключ структуры       |
| `DocumentTypeID` | INTEGER    | FK → `DocumentTypes.DocumentTypeID` | Ссылка на тип документа        |
| Doc`Metadata`    | JSONB      |                                     | Метаданные структуры документа |
| `CreatedAt`      | TIMESTAMP  | DEFAULT CURRENT\_TIMESTAMP          | Время создания записи          |
| `UpdatedAt`      | TIMESTAMP  | DEFAULT CURRENT\_TIMESTAMP          | Время последнего обновления    |
| `CreatedBy`      | INTEGER    | FK → `Employees.EmployeeID`         | Кто создал запись              |

#### Таблица `SEMDTemplates`

<table><thead><tr><th>Поле</th><th>Тип данных</th><th width="191.2000732421875">Ограничения</th><th>Описание</th></tr></thead><tbody><tr><td><code>TemplateID</code></td><td>SERIAL</td><td>PK</td><td>Первичный ключ шаблона</td></tr><tr><td><code>Name</code></td><td>VARCHAR(100)</td><td></td><td>Название шаблона</td></tr><tr><td>Semd<code>Metadata</code></td><td>JSONB</td><td></td><td>Метаданные структуры СЭМД</td></tr><tr><td><code>CreatedAt</code></td><td>TIMESTAMP</td><td>DEFAULT CURRENT_TIMESTAMP</td><td>Время создания записи</td></tr><tr><td><code>UpdatedAt</code></td><td>TIMESTAMP</td><td>DEFAULT CURRENT_TIMESTAMP</td><td>Время последнего обновления</td></tr><tr><td><code>CreatedBy</code></td><td>INTEGER</td><td>FK → <code>Employees.EmployeeID</code></td><td>Кто создал запись</td></tr></tbody></table>

#### Таблица `Settings`

| Поле         | Тип данных | Ограничения                 | Описание                    |
| ------------ | ---------- | --------------------------- | --------------------------- |
| `SettingID`  | SERIAL     | PK                          | Первичный ключ настройки    |
| `Parameters` | JSONB      |                             | Параметры настроек          |
| `CreatedAt`  | TIMESTAMP  | DEFAULT CURRENT\_TIMESTAMP  | Время создания записи       |
| `UpdatedAt`  | TIMESTAMP  | DEFAULT CURRENT\_TIMESTAMP  | Время последнего обновления |
| `CreatedBy`  | INTEGER    | FK → `Employees.EmployeeID` | Кто создал запись           |

#### Таблица `RefAddresses`

| Поле        | Тип данных   | Ограничения | Описание              |
| ----------- | ------------ | ----------- | --------------------- |
| `AddressID` | SERIAL       | PK          | Первичный ключ адреса |
| `Address`   | VARCHAR(255) |             | Адрес                 |

#### Таблица `RefProfilesMP`

| Поле        | Тип данных   | Ограничения | Описание                            |
| ----------- | ------------ | ----------- | ----------------------------------- |
| `ProfileID` | SERIAL       | PK          | Первичный ключ профиля              |
| `Name`      | VARCHAR(255) |             | Название профиля медицинской помощи |

#### Таблица `RefOrganizations`

| Поле             | Тип данных   | Ограничения | Описание                   |
| ---------------- | ------------ | ----------- | -------------------------- |
| `OrganizationID` | SERIAL       | PK          | Первичный ключ организации |
| `Name`           | VARCHAR(255) |             | Название организации       |

#### Таблица `RefDiseases`

| Поле        | Тип данных   | Ограничения | Описание                   |
| ----------- | ------------ | ----------- | -------------------------- |
| `DiseaseID` | SERIAL       | PK          | Первичный ключ заболевания |
| `Name`      | VARCHAR(255) |             | Название заболевания       |

#### Таблица `RefDrugs`

| Поле     | Тип данных   | Ограничения | Описание                 |
| -------- | ------------ | ----------- | ------------------------ |
| `DrugID` | SERIAL       | PK          | Первичный ключ препарата |
| `Name`   | VARCHAR(255) |             | Название препарата       |
