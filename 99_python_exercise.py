# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

# class Car(object):
#     def __init__(self, args):
#         self.manufacturer = args[0]
#         self.model = args[1]
#         self.displ = args[2]
#         self.year = args[3]
#         self.cyl = args[4]
#         self.trans = args[5]
#         self.drv = args[6]
#         self.cty = args[7]
#         self.hwy = args[8]
#         self.fl = args[9]
#         self.car_class = args[10]
#
#     def __repr__(self):
#         return("""제조사: {} / 모델: {} / 배기량: {} / 연식: {} / 기통: {} / 기어: {} / 구동방식: {} / 도시연비: {} / 고속도로 연비: {} / 연료: {} / 차종: {}"""
# .format(self.manufacturer, self.model, self.displ, self.year, self.cyl, self.trans, self.drv, self.cty, self.hwy, self.fl, self.car_class))
#
# file = open("C:/python_data/mpg.txt", "r")
# lines = file.readlines()
# split_lines =[]
#
# for l in lines:
#     l = l.replace("\n","")
#     temp = l.split(',')
#     split_lines.append(temp)
#
# cars = []
# for c in split_lines:
#     temp_car = Car(c)
#     cars.append(temp_car)
#
# del cars[0]

class Car(object):
    def __init__(self, car_data):
        car_data = car_data.split(",")
        self.manufacturer = car_data[0]
        self.model = car_data[1]
        self.displ = float(car_data[2])
        self.year = int(car_data[3])
        self.cyl = int(car_data[4])
        self.trans = car_data[5]
        self.drv = car_data[6]
        self.cty = int(car_data[7])
        self.hwy = int(car_data[8])
        self.fl = car_data[9]
        self.car_class = car_data[10]

    def __repr__(self):
        return self.manufacturer + ", " + self.model \
               + ", " + self.displ + ", " + self.year \
               + self.trans + ", " + self.drv \
               + self.cty + ", " + self.hwy




file = open("C:/python_data/mpg.txt","r")
car_list = list()

line = file.readline()

while True:
    line = file.readline()
    if not line:
        break
    car_list.append(Car(line.strip()))

file.close()

displ_4_lower = []
displ_5_upper = []

for tmp in car_list:
    if tmp.displ <=4:
        displ_4_lower.append(tmp.hwy)
    elif tmp.displ >= 5:
        displ_5_upper.append(tmp.hwy)

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))

## List Comprehension

displ_4_lower = [tmp.hwy for tmp in car_list if tmp.displ <= 4]
displ_5_upper = [tmp.hwy for tmp in car_list if tmp.displ >= 5]

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))

## filter 함수 이용

def filter_displ_4_lower(tmp):
        return tmp.displ <= 4

def filter_displ_5_upper(tmp):
    return tmp.displ >= 5

displ_4_lower_list = list(filter(filter_displ_4_lower,car_list))
displ_5_upper_list = list(filter(filter_displ_5_upper,car_list))

displ_4_lower = [tmp.hwy for tmp in displ_4_lower_list]
displ_5_upper = [tmp.hwy for tmp in displ_5_upper_list]

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))

## lambda 이용
displ_4_lower_list = list(filter(lambda tmp:tmp.displ <= 4,car_list))
displ_5_upper_list = list(filter(lambda tmp:tmp.displ >= 5,car_list))

displ_4_lower = [tmp.hwy for tmp in displ_4_lower_list]
displ_5_upper = [tmp.hwy for tmp in displ_5_upper_list]

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))


# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.

cty_audi_list = [tmp.cty for tmp in car_list if tmp.manufacturer == "audi"]
cty_toyota_list = [tmp.cty for tmp in car_list if tmp.manufacturer == "toyota"]

cty_audi = sum(cty_audi_list) / len(cty_audi_list)
cty_toyota = sum(cty_toyota_list) / len(cty_toyota_list)

print("audi의 평균 cty : {}".format(cty_audi))
print("toyota의 평균 cty : {}".format(cty_toyota))

# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
hwy_chevrolet_list = [tmp.hwy for tmp in car_list if tmp.hwy == "chevrolet"]
hwy_ford_list = [tmp.hwy for tmp in car_list if tmp.hwy == "ford"]
hwy_honda_list = [tmp.hwy for tmp in car_list if tmp.hwy == "honda"]

hwy_chevrolet = sum(hwy_chevrolet_list) / len(hwy_chevrolet_list)
hwy_ford = sum(hwy_ford_list) / len(hwy_ford_list)
hwy_honda = sum(hwy_honda_list) / len(hwy_honda_list)

print("chevrolet의 평균 hwy: {}".format(hwy_chevrolet))
print("ford의 평균 hwy: {}".format(hwy_ford))
print("honda의 평균 hwy: {}".format(hwy_honda))
# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.
audi_class = [tmp.car_class for tmp in car_list]
audi_class_set = set(audi_class)

def make_car_dict(car_class):
    result = [tmp.hwy for tmp in car_list if tmp.car_class == car_class]
    return(car_class)

my_result = []
for tmp in audi_class_set:
    my_result.append(make_car_dict(tmp))
    print("1위: {}".format())
    print("2위: {}".format())
    print("3위: {}".format())
    print("4위: {}".format())
    print("5위: {}".format())
# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

mpg_class = [tmp.car_class for tmp in car_list]
mpg_class_set = set(mpg_class)

def make_car_dict(car_class):
    result = [tmp.cty for tmp in car_list if tmp.car_class == car_class]
    avg = sum(result) / len(result)
    return (car_class, avg)

my_result = []
for tmp in mpg_class_set:
    my_result.append(make_car_dict(tmp))
kk = reversed(sorted(my_result, key=lambda t : t[1]))
for i in kk:
    print("class : {}, cty평균 : {}".format(i[0],i[1]))



# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.
hwy_audi_list = [tmp.hwy for tmp in car_list if tmp.hwy == "audi"]
hwy_chevrolet_list = [tmp.hwy for tmp in car_list if tmp.hwy == "chevrolet"]
hwy_dodge_list = [tmp.hwy for tmp in car_list if tmp.hwy == "dodge"]
hwy_ford_list = [tmp.hwy for tmp in car_list if tmp.hwy == "ford"]
hwy_honda_list = [tmp.hwy for tmp in car_list if tmp.hwy == "honda"]
hwy_hyundai_list = [tmp.hwy for tmp in car_list if tmp.hwy == "hyundai"]
hwy_jeep_list = [tmp.hwy for tmp in car_list if tmp.hwy == "jeep"]
hwy_landrover_list = [tmp.hwy for tmp in car_list if tmp.hwy == "landrover"]
hwy_lincoln_list = [tmp.hwy for tmp in car_list if tmp.hwy == "lincoln"]
hwy_mercury_list = [tmp.hwy for tmp in car_list if tmp.hwy == "mercury"]
hwy_nissan_list = [tmp.hwy for tmp in car_list if tmp.hwy == "nissan"]
hwy_pontiac_list = [tmp.hwy for tmp in car_list if tmp.hwy == "pontiac"]
hwy_subaru_list = [tmp.hwy for tmp in car_list if tmp.hwy == "subaru"]
hwy_toyota_list = [tmp.hwy for tmp in car_list if tmp.hwy == "toyota"]
hwy_volkswagen_list = [tmp.hwy for tmp in car_list if tmp.hwy == "volkswagen"]

hwy_audi = sum(hwy_audi_list) / len(hwy_audi_list)
hwy_chevrolet = sum(hwy_chevrolet_list) / len(hwy_chevrolet_list)
hwy_dodge = sum(hwy_dodge_list) / len(hwy_dodge_list)
hwy_ford = sum(hwy_ford_list) / len(hwy_ford_list)
hwy_honda = sum(hwy_honda_list) / len(hwy_honda_list)
hwy_hyundai = sum(hwy_hyundai_list) / len(hwy_hyundai_list)
hwy_jeep = sum(hwy_jeep_list) / len(hwy_jeep_list)
hwy_landrover = sum(hwy_landrover_list) / len(hwy_landrover_list)
hwy_lincoln = sum(hwy_lincoln_list) / len(hwy_lincoln_list)
hwy_mercury = sum(hwy_mercury_list) / len(hwy_lincoln_list)
hwy_nissan = sum(hwy_nissan_list) / len(hwy_nissan_list)
hwy_pontiac = sum(hwy_pontiac_list) / len(hwy_pontiac_list)
hwy_subaru = sum(hwy_subaru_list) / len(hwy_subaru_list)
hwy_toyota_list = sum(hwy_toyota_list) / len(hwy_toyota_list)
hwy_volkswagen = sum(hwy_volkswagen_list) / len(hwy_volkswagen_list)



# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.



