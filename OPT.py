import re,string
MSGS = [
"AFCD528030FBA2EF61C94A3932AD8ED3E5340216025FB57FD577B7440E04EC63061570F7EC852F3013B5797CFBA6A3DAD2CB82449E2CC4D7721FD01A7285AE441FB88553C5B0B925ABFFC0A16AE82FF2809FAF3111E90B5C99291A9A42C5D67838AC0DF52F18D6C32DE889FC0E00B532D3C62393C20E857C6ED5373093E083290C388AD959B7FC8C9240F006B8D4A439F5A45AE00FA8EF12805F78D2DF0F23FB0C9E72FA8D2DBF380B",
"A6D1059C29EBF0AC79C81F7C30BF899FFD781F165643A57FD577B7485D57FD65110F34A0E68C2E7301FA633AB5B7A3C686868B4A9F2ED9907315D10C7283AE5D07F19F498CA7F114E3F4D2E276EE24BD8299AE7F5EF64448993E17865C82D9783AA60CBC295686D831BC8DAE4D18F124D5DB719E8D14D73F78D3762C97E0837B4D7D94CF4FE2E997C714E80BA995A539",
"BAD61B8A7FFAEDE36C871D3D20FE84CDF975181C1216B47F9662AA524B57FE65490C75B9FA8C24730AF4787EB4BFE6D6C3939A0B9728C5D77005D05F2592A90517B4854ECBBDEA5FE3C1DBE473A921B7D784A23046B00509DD3F019C528B972C33E91FBC2B1A9FD22CBC",
"99DB528E3EE0F6AC74C84A3432A8829FEF7B011C5642B3628123AB494F03A964061E67B9A99D603E1DF4783ABABCBFD6CE82804CD12ED9D76F11D00B3B94BE4912A3D64DD9A0ED51B7F993E873ED3FB19683AF7F45F8055D99781A90478097312FE909F42D04939736A08DFC1909A4239DC56A86C15BC77A2D",
"CECA1A982BAEE5E974D44A3036B8939FE87B4C0E1E5FB5729075BA530E1EE7740C097AF7F98833730DFB7075A9A6B3CCC79F8B0B9429D8827818820B3DD7BC441FBAD641C5A1EA05E3FFDDF572A922BA92D7A53957F9074C992E1A9441C5D33925E75ED5260586DE30AD8CFC0F15FC23D5DB70CADE12D16A6ECF7E379C",
"CEFF1E957FCFE0E375D34A1F3AAC84CAF5601F591F45F66A8061B3485D1FE06E0E5B75F7FD8C323A1DE63675BDF2A7D0D2828D47943497987150C7123092AF4116B5D654C9B0EC03AAE2CAA16AE022BAD796EA2C45E20B47DE7A149A5690C47833A75EF22D0281D830A3C8AF080FA925D4C67A",
"BACC0BD937EFF0E865D54A313CAD939FF3724C0D1E5FA53A8166A7550E1EFA20041E75B9E787273F1DE6653BFBA7A8CEC3989D0B8828C2D7791FC10A21D7A44B53A59E428CBEF818ADB6C7E06FEE33A6D780A23652F84440CA7A069D50C5DC3D25E91CE53C1385972DA684A5",
"AFCD018C32EBA2F868C61E7C3AFE8FDEEA714C1D1350BF749067FF4F4B00A952081570B8E3C1746151B57F74FBB1AAC3D598CE4A9F23979E7150C3113D83A34001F1954BCDA0EA51AAB6D2E67CE038F29398EA3154E7447BD834169A58CD9E7833A712E5681798D362A1C8BB0218FC33D4D4658FDF1ECB6B2FC9722B87FA9227433691CF0AB6F89DC051B806A28DF628E3A25FEC0ABCE957D4437593CD4624BA03DF6CA8912CBE7B0DC0EBD0A59CA431BFDDE60C057AF79C78452A98D4D3928CBB92E14C84CCFAFB05C46671F7AB52E2B9A670EEE004DED41AFE7F5358A2417C0D1C4AAFB60722EC294ED3ADE172D69B7272FEBA4FC573ABAF62DC1740A433C1E749A656DA0CB1C17C543AEA755B5BAD57542FFBA10976C305A00A70706491FA15E8BE1FBB082B1B63791813AC0E1118AAAE88E2A1C2DC7ABA9FFA8C52750FE6F4DC",
"BAD6138D78FDA2F868C24A2C21B789DCF564001C5659B03A94238F524B02ED6F44295A90A0C9143B1DB5786FB6B0A3D0D5CB8F599467D9986B50D01A339BA75C53A39749C8BCF4",
"BAD617807FEFF0E920C00F3236AC86CBF9704C0C055FB87DD562FF454B03EC7204127ABEFD9D293058F47A7DB4A0AFD6CE86"]


Cipher = "BAD617D92CEBE1FE65D34A3136AD94DEFB714C10050CF64D9D66B1015B04E06E0E5B75F7FD9D323619F83679B2A2AEC7D4CB804E8722C5D76A03C75F269FAE0518B48F07C1BCEB14E3E2DBE073A939BC9492EA7700A8561E886C4BDC"
###    equal in length

l=len(Cipher)
for index,msg in enumerate(MSGS):
    if len(msg)<l:
        MSGS[index]=MSGS[index]+Cipher[len(MSGS[index]):]
    elif len(msg)>l:
        MSGS[index]=msg[:l]

###

def xor(x,y):
    return x^y

###viable pool
#adding numbers leades to code + CHAOSSSSSS
possibleLetters= list(string.ascii_letters)
possibleLetters.append(' ')



#### numbers cause chaos
# h=list(string.digits)
# for i  in h:
#     possibleLetters.append(i)

for i in range(len(possibleLetters)):
    possibleLetters[i]=ord(possibleLetters[i])

possibleLetters.reverse()

def IS_VIABLE_LETTER(x):
    if x in possibleLetters:
        return 1
    else:
        return 0
#pair of hexadica

Cipher=re.findall('..', Cipher)

for i in range (len(MSGS)):
    MSGS[i]=re.findall('..', MSGS[i])


##eazy xor / ascii
for index,letter in enumerate(Cipher):
    Cipher[index]=int(letter,16)
for i in range(len(MSGS)):
    for index,letter in enumerate(MSGS[i]):
        MSGS[i][index]=int(letter,16)


## get plaintext of MSGS xor plain text of Cypher
for i in range(len(MSGS)):
    for index, letter in enumerate(MSGS[i]):
        MSGS[i][index]=xor(Cipher[index],MSGS[i][index])



for letter in range(len(Cipher)):

    for potential in possibleLetters:
        truth = []
        for i in range(len(MSGS)):
            truth.append(0)
        for i in range(len(MSGS)):
            truth[i]=IS_VIABLE_LETTER(xor(potential,MSGS[i][letter]) )
        if(truth.count(1)==len(truth)):
            Cipher[letter]=potential

str=""

for letter in range(len(Cipher)):
    str=str+chr(Cipher[letter])
print((str))