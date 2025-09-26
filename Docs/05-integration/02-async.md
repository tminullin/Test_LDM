# 5.2 Асинхронная отправка результата регистрации СЭМД

### 1. Общие сведения

#### 1.1 Наименование операциии

Асинхронная отправка результата регистрации сведений  СЭМД в ИС Поликлиника их ФХ СЭМД

#### 1.2 Назначение

Метод предназначен для асинхронной передачи в ИС Поликлиника результатов регистрации сведений об электронных медицинских документах (СЭМД) от ФХ СЭМД через очередь сообщений Apache Kafka.

### 2. Описание

#### 2.1 Компоненты системы

* Producer: ФХ СЭМД&#x20;
* Consumer: ИС Поликлиника
* Message Broker: Apache Kafka
* REST API Endpoint: HTTP endpoint в ИС Поликлиника

#### 2.2 Схема взаимодействия

```
ФХ СЭМД → Kafka Topic → ИС Consumer → Обработчик сообщения
```

### 3. Технические требования

#### 3.1 Структура топика

**Topic Name**: `semd-registration-results`

**Формат сообщения**: JSON



**Заголовок сообщения**&#x20;

```json
{
  "messageType": "REGISTRATION_RESULT",
  "sourceSystem": "FH_SEMD",
  "targetSystem": "IS",
  "messageId": "uuid",
  "timestamp": "2025-01-15T10:30:00.000Z"
}
```

**Тело сообщения**

```json
{
  "relatesToMessage": "string",
  "status": "success|error",
  "registryItem": {
    "emdrId": "string",
    "documentVersion": "integer",
    "registrationDate": "datetime",
    "registrationDateTime": "datetime", 
    "storeTillDate": "date",
    "registrationWarnings": [
      {
        "code": "string",
        "message": "string"
      }
    ]
  },
  "errors": [
    {
      "code": "string",
      "message": "string"
    }
  ]
}
```

#### 3.3 Описание запроса REST API

**Запрос**

```http
POST /api/v1/internal/semd/registration-result
Content-Type: application/json
```

**Тело запроса**:

```json
{
  "relatesToMessage": "string",
  "status": "success|error",
  "errors": [ ... ]
}
```

**Тело ответа**:

```json
{
  "status": "success|error",
  "errors": [
    {
      "code": "string",
      "message": "string"
    }
  ]
}
```

#### 3.4 Логика работы обработчика

1. Поиск исходного запроса: по `relatesToMessage`
2. Обновление статуса: в базе данных ИС
3. Формирование ответа



