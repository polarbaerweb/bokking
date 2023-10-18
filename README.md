**Главная страница:** пользователи должны иметь возможность просмотреть все будущие сеансы на главной странице !DONE

**Страница фильма:** на странице фильма пользователь должен иметь возможность увидеть название, постер, описание, рейтинги фильма и список актеров, которые играли в этом фильме, а также список режиссеров, продюсеров и т.д. !DONE

- Также на этой странице пользователь должен иметь возможность перейти на страницу выбора кинотеатра и зала, где показывается данный фильм

       **Страница выбора кинотеатра и зала:** на этой странице должен быть список кинотеатров с подсписком сеансов для каждого кинотеатра, в информации сеанса должны быть указаны: зал, время начала и диапазон цен на этот сеанс (мин. цена - макс. цена, соответственно у некоторых рядов цена может быть выше чем у других).


      **Страница заказа билета:** на этой странице пользователь должен видеть кресла так, как они расположены в кинотеатре, а также должен иметь возможность выбрать одно или несколько кресел для брони по желанию.

      **Страница бронирования**: на этой странице пользователь должен иметь возможность ввести свои данные(если не авторизован), просмотреть общую стоимость и подтвердить бронь.

      **Страница с билетом:** после подтверждения брони пользователь должен быть перенаправлен на страницу с билетом, где должен быть указан id его билета, и ссылка, при переходе по которой всегда будет открываться данный билет.

- Также на странице должна быть полная информация о том какие места были забронированы.

      **Логин/Логаут:** тут все и так ясно !DONE

      **Страница пользователя:** на собственной странице пользователь должен иметь возможность посмотреть все свои прежние и текущие брони

**Если пользователь является админом:** у него должна быть возможность из главной страницы перейти на страницы:

- **История всех броней:** где админ может посмотреть подробный список всех броней (Имя пользователя, фильм, дата показа, забронированные места, сумма оплаты);
  - Имя пользователя для конкретной брони должно быть ссылкой и вести на страницу пользователя, где админ может посмотреть все брони пользователя.
  - Если бронь выполнена без входа (пользователь отсутствует), то имя пользователя не является ссылкой
  - Фильм должен быть ссылкой и вести на страницу фильма
  - Дата показа должна быть ссылкой и вести на страницу, где отображаются все сеансы, запланированные на этот день
- **Добавить новый сеанс:** где админ может добавить новый сеанс выбрав фильм, дату сеанса, кинотеатр и зал в этом кинотеатре (учитывая, что зал и кинотеатр связаны, после выбора кинотеатра из выпадающего списка, админ должен иметь возможность выбрать только из списка залов в этом кинотеатре в выпадающем списке с залами);
- **Управление кинотеатрами:** где админ может добавить новый кинотеатр и залы для этого кинотеатра или изменить уже существующий;
- **Управление сеансами и фильмами:** где админ будет иметь возможность изменить или удалить существующие сеансы для конкретных кинотеатров/залов или целиком из показа;
