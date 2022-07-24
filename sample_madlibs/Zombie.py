def madlib():
    time_of_day = input("Hora do dia: ")
    body_part_plural = input("Parte do corpo (Plural): ")
    color = input("Cor: ")
    verb_past_tense = input("Verbo(passado): ")
    food = input("Comida: ")
    noun1 = input("Substantivo: ")
    noun_plural_1 = input("Substantivo (plural): ")
    adj1 = input("Adjetivo: ")
    adj2 = input("Adjetivo: ")
    adj3 = input("Adjetivo: ")

    madlib = f"Era um {adj1} verão {time_of_day} quando percebemos que a vacina iria parar \
     propagação da doença não funcionou. Em vez disso produziu ZOMBIS!!!{body_part_plural} \
    e as ruas estavam alinhadas com esses monstros segurando{noun_plural_1} em suas mãos. \
    Seus olhos estam {color} com fome como eles {verb_past_tense} pela cidade procurando {food}. \
    Eles eram {adj2} e {adj3}, sem saber como agir neste mundo... exceto comer {body_part_plural}!!!! \
    Essa era a sua única missão e eles se dedicaram a alcançá-la em nome da {noun1}."

    print(madlib)