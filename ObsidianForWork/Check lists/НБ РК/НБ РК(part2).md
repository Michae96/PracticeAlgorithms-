Для каждого из полей форм №9, №10, №11 и №12 опишу, примерно какие данные необходимо подтянуть из базы:

---
### Форма №9
**Сведения о количестве агентов и субагентов эмитента электронных денег и владельцев электронных денег**
1. **Наименование системы**  
   - Статичное значение: `"ТОО One Vision"`.
2. **Всего агентов**  
   - Количество всех агентов, зарегистрированных в системе.
   - Таблица `agents`, например: `SELECT COUNT(*) FROM agents`.
3. **Активных агентов**  
   - Количество агентов, которые совершили хотя бы одну транзакцию за указанный период.
   - Таблицы `agents` и `transactions`, например:
     ```sql
     SELECT COUNT(DISTINCT agent_id) 
     FROM transactions 
     WHERE transaction_date BETWEEN [start_date] AND [end_date];
     ```
4. **Всего субагентов**  
   - На данный момент значение равно 0, так как в системе нет субагентов.
5. **Активных субагентов**  
   - Значение также равно 0, поскольку отсутствуют субагенты.
6. **Всего кошельков**  
   - Общее количество кошельков физических лиц.
   - Таблица `wallets`, например: `SELECT COUNT(*) FROM wallets WHERE owner_type = 'physical'`.
7. **Активных кошельков**  
   - Количество кошельков, у которых были транзакции в указанный период.
   - Таблицы `wallets` и `transactions`, например:
     ```sql
     SELECT COUNT(DISTINCT wallet_id) 
     FROM transactions 
     WHERE owner_type = 'physical' AND transaction_date BETWEEN [start_date] AND [end_date];
     ```
8. **Идентифицированных кошельков**  
   - Количество кошельков с идентификацией `basic` или `full`.
   - Таблица `wallets`, например: `SELECT COUNT(*) FROM wallets WHERE owner_type = 'physical' AND identification_status IN ('basic', 'full')`.
9. **Всего кошельков мерчантов**  
   - Общее количество мерчантских кошельков.
   - Таблица `wallets`, например: `SELECT COUNT(*) FROM wallets WHERE owner_type = 'merchant'`.
10. **Активных кошельков мерчантов**  
    - Количество мерчантских кошельков, у которых были транзакции в указанный период.
    - Таблицы `wallets` и `transactions`, например:
      ```sql
      SELECT COUNT(DISTINCT wallet_id) 
      FROM transactions 
      WHERE owner_type = 'merchant' AND transaction_date BETWEEN [start_date] AND [end_date];
      ```




---
### Форма №10
**Сведения о количестве и объемах операций, проведенных с использованием электронных денег**
1. **Система**  
   - Статичное значение: `"ТОО One Vision"`.
2. **Окружение**  
   - Текущая среда работы (например, `"система электронных денег"`).
3. **Количество операций на кошельки**  
   - Количество транзакций, совершенных в пользу физических лиц.
   - Таблица `transactions`, например:
     ```sql
     SELECT COUNT(*) 
     FROM transactions 
     WHERE owner_type = 'physical' AND transaction_date BETWEEN [start_date] AND [end_date];
     ```
4. **Сумма операций на кошельки**  
   - Суммарный объем транзакций для физических лиц.
   - Таблица `transactions`, например:
     ```sql
     SELECT SUM(amount) 
     FROM transactions 
     WHERE owner_type = 'physical' AND transaction_date BETWEEN [start_date] AND [end_date];
     ```
5. **Количество операций на мерчантов**  
   - Количество транзакций для мерчантских кошельков.
   - Таблица `transactions`, например:
     ```sql
     SELECT COUNT(*) 
     FROM transactions 
     WHERE owner_type = 'merchant' AND transaction_date BETWEEN [start_date] AND [end_date];
     ```
6. **Сумма операций на мерчантов**  
   - Суммарный объем транзакций для мерчантов.
   - Таблица `transactions`, например:
     ```sql
     SELECT SUM(amount) 
     FROM transactions 
     WHERE owner_type = 'merchant' AND transaction_date BETWEEN [start_date] AND [end_date];
     ```




---
### Форма №11
**Сведения о количестве электронных денег в обращении и о количестве и объемах операций по выпуску и погашению электронных денег**
1. **Владельцы электронных денег**  
   - **Агенты эмитента** - статичное значение `"One Vision"`.
   - **Субагенты эмитента** - значение 0, поскольку субагенты не заданы.
   - **Физические лица** - кошельки с `owner_type = 'physical'`.
   - **ИП и юридические лица** - кошельки с `owner_type = 'merchant'`.
2. **Наименование системы**  
   - Статичное значение: `"ТОО One Vision"`.
3. **Электронные деньги в обращении (тенге)**  
   - Баланс для каждой категории:
     - **Агенты эмитента**: общий баланс.
     - **Физические лица** и **ИП/юридические лица** — подсчитываем по `owner_type`.
     - Таблица `wallets`, например: `SELECT SUM(balance) FROM wallets WHERE owner_type = 'physical'` и аналогично для `merchant`.
4. **Количество операций выпуска**  
   - Количество транзакций по выпуску для каждой категории.
   - Таблица `transactions`, например:
     ```sql
     SELECT COUNT(*) 
     FROM transactions 
     WHERE operation_type = 'release' AND owner_type = 'physical' AND transaction_date BETWEEN [start_date] AND [end_date];
     ```
5. **Сумма выпуска (тенге)**  
   - Сумма выпуска для каждой категории.
   - Таблица `transactions`, аналогично запросу выше, но с `SUM(amount)` вместо `COUNT(*)`.
6. **Количество операций погашения**  
   - Количество транзакций по погашению для каждой категории.
   - Таблица `transactions`, например:
     ```sql
     SELECT COUNT(*) 
     FROM transactions 
     WHERE operation_type = 'redemption' AND owner_type = 'physical' AND transaction_date BETWEEN [start_date] AND [end_date];
     ```
7. **Сумма погашения (тенге)**  
   - Сумма погашения для каждой категории.
   - Таблица `transactions`, аналогично запросу выше, но с `SUM(amount)` вместо `COUNT(*)`.




---
### Форма №12
**Сведения о количестве и объемах операций по приобретению и реализации электронных денег агентами эмитента электронных денег**
1. **Тип операции**  
   - Статичные строки: `"Реализация агентами"`, `"Реализация субагентами"`, `"Приобретение агентами"`, `"Приобретение субагентами"`.
2. **Количество операций**  
   - Число операций по каждому типу.
   - Таблица `transactions`, фильтрация по `operation_type` для каждого типа.
3. **Сумма (тенге)**  
   - Сумма операций для каждого типа.
   - Таблица `transactions`, фильтрация и агрегация по `amount` для каждого типа операции.