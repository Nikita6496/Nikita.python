
import sqlite3 as sq

with sq.connect("company_strah.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS services")
    cur.execute("""CREATE TABLE IF NOT EXISTS services(data_zak date not null,
    strah_sum decimal(10,2) not null, strah_type text not null, stavka decimal(5,2) not null,
    filial varchar(20) not null)""")

    information = [
        ("10.10.2020 10:10:10", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:11", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:12", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:13", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:14", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:15", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:16", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:17", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:18", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:19", 100000, "Страхование жизни", 30, "Первый филиал")
    ]
    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?)", information)

    #cur.execute("SELECT * FROM services WHERE surname_klient = ?", ("Морозова",))
    #print(cur.fetchall())
    #cur.execute("SELECT * FROM services WHERE notary_type = ?", ("Договор купли-продажи квартиры",))
    #print(cur.fetchall())
    #cur.execute("SELECT surname_klient,notary_type,sum_of_transaction,dohod FROM services WHERE dohod > ?",(1000,))
    #print(cur.fetchall())

    #cur.execute("DELETE FROM services WHERE surname_klient = ?", ("Петрова",))
    #cur.execute("DELETE FROM services WHERE sum_of_transaction < ?", (2600,))
    #cur.execute("DELETE FROM services WHERE dohod > ?", (1000,))

    #cur.execute("UPDATE services SET notary_type = ? WHERE surname_klient = ? AND name_klient = ? AND lastname_klient = ?",("Продажа дачного участка", "Федорова", "Мария", "Олеговна"))
    #cur.execute("UPDATE services SET sum_of_transaction = ? WHERE surname_klient = ? AND name_klient = ? AND lastname_klient = ?",(3500, "Смирнова", "Анна", "Владимировна"))
    #cur.execute("UPDATE services SET dohod = ? + 500 WHERE notary_type = ?",(1300, "Продажа коммерческой недвижимости"))