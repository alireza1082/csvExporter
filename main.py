import pandas as panda


def print_hi(name):
    print(f"Hi {name}")
    file = panda.read_csv("./datas/cy68j2_posts.csv")
    coupons = file.loc[file['post_type'] == 'shop_coupon']

    print(coupons)
    coupons.to_csv('./outs/coupons.csv')


if __name__ == '__main__':
    print_hi('alireza')
