from pathlib import Path
from sys import path


def search_context(keyword, *keywords, context=0):
    result = []
    intial_Path = Path(path[0])
    data_Path = intial_Path / "data"
    for path_ in data_Path.glob('*.txt'):
        with open(path_,'r',encoding='utf-8') as file:
            lines = file.readlines()           
            for line_number, line in enumerate(lines):
                line_lower = line.lower()
                if any(kw.lower() in line_lower for kw in (keyword, *keywords)):
                    context_lines = lines[max(0, line_number - context):line_number + context + 1]
                    context_text = ''.join(context_lines).strip()
                    
                    result.append({
                        'keyword': keyword,
                        'filename': path_.name,
                        'line': line_number + 1,
                        'context': context,
                        'text': context_text
                    })
    
    return result

# >>> from pprint import pprint
# >>> pprint(search_context('мысль', 'мысли'))
# [{'context': 0,
  # 'filename': 'E3ln1.txt',
  # 'keyword': 'мысль',
  # 'line': 147,
  # 'text': '- А знаете, Павел Иванович, - сказал Манилов, которому очень '
          # 'понравилась такая мысль, - как было бы в самом деле хорошо, если бы '
          # 'жить этак вместе, под одною кровлею, или под тенью какого-нибудь '
          # 'вяза пофилософствовать о чем-нибудь, углубиться!..'},
 # {'context': 0,
  # 'filename': 'E3ln1.txt',
  # 'keyword': 'мысль',
  # 'line': 163,
  # 'text': 'Манилов долго стоял на крыльце, провожая глазами удалявшуюся '
          # 'бричку, и когда она уже совершенно стала не видна, он все еще '
          # 'стоял, куря трубку. Наконец вошел он в комнату, сел на стуле и '
          # 'предался размышлению, душевно радуясь, что доставил гостю своему '
          # 'небольшое удовольствие. Потом мысли его перенеслись незаметно к '
          # 'другим предметам и наконец занеслись бог знает куда. Он думал о '
          # 'благополучии дружеской жизни, о том, как бы хорошо было жить с '
          # 'другом на берегу какой-нибудь реки, потом чрез эту реку начал '
          # 'строиться у него мост, потом огромнейший дом с таким высоким '
          # 'бельведером, что можно оттуда видеть даже Москву, и там пить '
          # 'вечером чай на открытом воздухе и рассуждать о каких-нибудь '
          # 'приятных предметах. Потом, что они вместе с Чичиковым приехали в '
          # 'какое-то общество в хороших каретах, где обворожают всех '
          # 'приятностию обращения, и что будто бы государь, узнавши о такой их '
          # 'дружбе, пожаловал их генералами, и далее, наконец, бог знает что '
          # 'такое, чего уже он и сам никак не мог разобрать. Странная просьба '
          # 'Чичикова прервала вдруг все его мечтания. Мысль о ней как-то '
          # 'особенно не варилась в его голове: как ни переворачивал он ее, но '
          # 'никак не мог изъяснить себе, и все время сидел он и курил трубку, '
          # 'что тянулось до самого ужина.'},
 # {'context': 0,
  # 'filename': 'le1UO.txt',
  # 'keyword': 'мысль',
  # 'line': 13,
  # 'text': 'Как и все старые люди вообще, графиня страдала бессонницею. '
          # 'Раздевшись, она села у окна в вольтеровы кресла и отослала '
          # 'горничных. Свечи вынесли, комната опять осветилась одною лампадою. '
          # 'Графиня сидела вся желтая, шевеля отвислыми губами, качаясь направо '
          # 'и налево. В мутных глазах ее изображалось совершенное отсутствие '
          # 'мысли; смотря на нее, можно было бы подумать, что качание страшной '
          # 'старухи происходило не от ее воли, но по действию скрытого '
          # 'гальванизма.'},
 # {'context': 0,
  # 'filename': 'r62Bf.txt',
  # 'keyword': 'мысль',
  # 'line': 19,
  # 'text': 'Вдруг он вздрогнул: одна, тоже вчерашняя, мысль опять пронеслась в '
          # 'его голове. Но вздрогнул он не оттого, что пронеслась эта мысль. Он '
          # 'ведь знал, он предчувствовал, что она непременно «пронесется», и '
          # 'уже ждал ее; да и мысль эта была совсем не вчерашняя. Но разница '
          # 'была в том, что месяц назад, и даже вчера еще, она была только '
          # 'мечтой, а теперь… теперь явилась вдруг не мечтой, а в каком-то '
          # 'новом, грозном и совсем незнакомом ему виде, и он вдруг сам сознал '
          # 'это… Ему стукнуло в голову, и потемнело в глазах.'},
 # {'context': 0,
  # 'filename': 'r62Bf.txt',
  # 'keyword': 'мысль',
  # 'line': 61,
  # 'text': 'Несмотря на эти странные слова, ему стало очень тяжело. Он присел '
          # 'на оставленную скамью. Мысли его были рассеянны… Да и вообще тяжело '
          # 'ему было думать в эту минуту о чем бы то ни было. Он бы хотел '
          # 'совсем забыться, все забыть, потом проснуться и начать совсем '
          # 'сызнова…'},
 # {'context': 0,
  # 'filename': 'r62Bf.txt',
  # 'keyword': 'мысль',
  # 'line': 63,
  # 'text': '«А куда ж я иду? - подумал он вдруг. - Странно. Ведь я зачем-то '
          # 'пошел. Как письмо прочел, так и пошел… На Васильевский остров, к '
          # 'Разумихину я пошел, вот куда, теперь… помню. Да зачем, однако же? И '
          # 'каким образом мысль идти к Разумихину залетела мне именно теперь в '
          # 'голову? Это замечательно».'}]
# >>> 