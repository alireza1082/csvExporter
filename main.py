import pandas as panda


def print_hi(name):
    print(f"Hi {name}")
    coupons = panda.read_csv("./datas/coup.csv")
    mobiles = panda.read_csv("./datas/numbers.csv")

    out = panda.merge(coupons, mobiles, on=["created_date"])
    print(out)
    out.to_csv('./outs/out.csv')


def get_coupons(path):
    file = panda.read_csv(path)
    coupons = file.loc[file['post_type'] == 'shop_coupon']

    print(coupons)
    coupons.to_csv('./outs/coupons.csv')


if __name__ == '__main__':
    print_hi('alireza')
