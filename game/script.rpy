﻿define a=Character('Вы', color = "#fa8072")
define b=Character('Директор', color = "#228b22")
image school = "bg school.jpeg"
image school = "bg schoolcor.jpeg"
image school = "bg schoolcab1.jpeg"
label start :
    scene bg school
    a "Все произошло так быстро."
    a "Неделю назад меня исключили из школы за плохую учебу."
    a "И прямо сейчас я  стою перед новой."
    a "Я пообещал родителям учиться лучше, и они уверены, что это в моих силах."
    a "Но уверен ли в этом я сам?"
    a"Я знаю одно. Мне предстоит тяжелый год, и я хочу справиться."
    scene bg schoolcor with fade
    a"Я зашел в коридор, но здесь было почти пусто."
    a"О боже, я опоздал уже на 10 минут."
    a"Хорошо начался мой первый день  в новой школе."
    scene bg schoolcab with dissolve
    a"Я зашел в кабинет."
    a"Здесь проходила физика, но надолго задержаться я здесь не успел."
    scene bg cabdirector with fade
    a"Так как меня вызвал директор."
    b"Здравствуйте.Меня зовут Николай Александрович. Для успешного поступления в школу вы должны пройти вступительный тест без единой ошибки."
    a"'Меня же никто не предупреждал.'-подумал я. Ну ладно я справлюсь."
    b"Ну что же, тогда приступим. Всего будет 10 вопросов, но помните ни единой ошибки.Так как вы почти закончили 10 класс в вашей предыдущей школе, программа будет соответствующая."
    b"Итак первый вопрос будет по русскому языку. Какое из иноязычных слов написано правильно?"
    menu:
          "Каппучино.":
              jump false
              
    
          "Фальстарт.":
              jump great
              
            
          "Координально.":
               jump false
            
        
label great:
     b"Правильный ответ."
     jump next
label false:
     b"Увы. Вы провалили тест."
     return
label next:
    b"Следующий вопрос будет по английскому языку. Как звучит поговорка 'Ни пуха, ни пера' на английском языке?"
    menu:
        "Break a leg.":
            jump great1
        
        "Throw caution to the winds.":
            jump false1
        
        "As right as rain.":
            jump false1
label great1:
    b"Ты просто гений."
    jump next1
label false1:
    b"Увы.Вы провалили тест."
    return
label next1:
    b"Ну что же.Следующий вопрос будет по алгебре.Решите уравнение log3(5х – 1) = 2"
    menu:
        "Ответ 1,5.":
            jump false2
        
        "Ответ 2.":
            jump great2
        
        "Ответ 3.":
            jump false2
label great2:
    b"Ты идешь очень хорошо.Продолжай."
    jump next2
label false2:
    b"Увы.Вы провалили тест."
    return
label next2:
    b"3 вопроса позади.Посмотрим как вы ответите на вопрос по геометрии. Сколько получится если в любом выпуклом многограннике сложить числа граней и вершин и вычесть число ребер?"
    menu:
        "Ответ 33.":
            jump false3
        
        "Ответ 0.":
            jump false3
        
        "Ответ 2.":
            jump great3
label great3:
    b"Ты идешь очень хорошо.Продолжай."
    jump next3
label false3:
    b"Увы.Вы провалили тест."
    return
label next3:
    b"Не понимаю. Откуда вы так много знаете? У меня написано, что вы плохо учились.Ладно, информатика."
    b"Как записывается оператор остановки цикла в C#?"
    menu:
        "End.":
            jump false4
        
        "Break.":
            jump great4
        
        "Stop.":
            jump false4
label great4:
    b"Поразительно.Опять правильно!!!"
    jump next4
label false4:
    b"Увы.Вы провалили тест."
    return
label next4:
    b"Хорошо.Я надеюсь, вы знаете историю? Следующий вопрос как раз по этой теме)"
    b"При каком правителе, было свергнуто монголо-татарское иго?"
    menu:
        "Иван Третий.":
            jump great5
        
        " Владимир.":
            jump false5
        
        "Всеволод Большое Гнездо.":
            jump false5
label great5:
    b"Вы интеллектуал."
    jump next5
label false5:
    b"Увы.Вы провалили тест."
    return
label next5:
    b"Давайте без лишних слов. Следующий вопрос по обществознанию."
    b"Что такое антропогенез?"
    menu:
        "Научное исследование происхождения человека.":
            jump great6
        
        "Слияние слоев общества.":
            jump false6
        
        "Духовное восприятие мира.":
            jump false6
label great6:
    b"Вы опять правы."
    jump next6
label false6:
    b"Увы.Вы провалили тест."
    return
label next6:
    b"Хорошо.Вопрос по географии."
    b"Столица Бразилии?"
    menu:
       "Бразилиа.":
            jump great7
        
       "Рио-Де-Жанейро.":
            jump false7
        
       "Сан-Паулу.":
            jump false7
label great7:
    b"Вы меня удивляете все больше и больше."
    jump next7
label false7:
    b"Увы.Вы провалили тест."
    return
label next7:    
    b"Биология.В Европе это насекомое называют божественный телёнок.Сможете ли вы сказать, как его называют у нас?"
    menu:
       "Жук-олень.":
            jump false8
        
       "Божья коровка.":
            jump great8
        
       "Шмель.":
            jump false8
label great8:
    b"Вы правильно ответили уже на ВОСЬМОЙ вопрос.Вы не задумывались о поступлении в университет?"
    jump next8
label false8:
    b"Увы.Вы провалили тест."
    return
label next8:
    b"Ладно следующий вопрос будет по физике.Скажите, что такое усиление света в результате вынужденного излучения?"
    menu:
       "Лазер.":
            jump great9
        
       "Радиация.":
            jump false9
        
       "Солнечная вспышка.":
            jump false9
label great9:
    b"Опять правильно."
    jump next9
label false9:
    b"Увы.Вы провалили тест."
    return
label next9:
    b"Ну что же. Последний вопрос будет по литературе"
    b"Кому принадлежит фраза 'Cамолюбие соль жизни'"
    menu:
       "Обломов.":
            jump great10
        
       "Печорин.":
            jump false10
        
       "Гринёв.":
            jump false10
label great10:
    b"Вы ответили на все 10 вопросов правильно"
    jump next10
label false10:
    b"Увы.Вы провалили тест."
    return
label next10:
    b"Вы успешно закончили тест.Вы определенно нужны нашей школе.Поздравляю вас."
    a "'Я очень рад!!!'-ответил я"
    a"В будущем я поступил в престижный университет.Нашел себе хорошую работу и сделал успешную карьеру"
    a"Школа помогла мне в жизни, и я это ценю"
    return
    
    
    
    
    
    
       
    
    
    
           
           

