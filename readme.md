# BTC_Rate_DAG
## Состав
- шаг создания таблицы в PG
- шаг запроса к API
- шаг вставки данных в таблицу PG

## Параметры
- rateDate (по умолчнию `latest`, принимает значения в формате `YYYY-MM-DD` для загрузки курсов за предыдущие даты)

## Порядок запуска
- `docker-compose up airflow-init`
- `docker-compose up`
- `http://localhost:8080/tree?dag_id=BTC_Rate_DAG`

## Проверка
- `http://localhost:5050/browser/`
- `User ID=airflow; Password=airflow; Host=postgres-out; Port=5432; Database=airflow-out;`
- в таблицу `out_table` выгражаются записи
```
    pair - наименование валютной пары
    ratedate - дата получения курса
    rate - курс валютной пары
```

## Примечания
- Т.к. в задании указано сохранить валютную пару, дату и текущий курс, первичный ключ таблицы - составной (`pair, ratedate`), а при повторной загрузке данных за однк и ту-же дату происходит обновление значения `rate`