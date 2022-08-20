#ajoute K, M, B, AA, AB, AC etc...
def AdaptMoney(money_before):
    if money_before >= 10**18:
        money_divide = round(money_before / 10**18, 2)
        money_after = (str(money_divide) + " AC")
    elif money_before >= 10**15:
        money_divide = round(money_before / 10**15, 2)
        money_after = (str(money_divide) + " AB")
    elif money_before >= 10**12:
        money_divide = round(money_before / 10**12, 2)
        money_after = (str(money_divide) + " AA")
    elif money_before >= 10**9:
        money_divide = round(money_before / 10**9, 2)
        money_after = (str(money_divide) + " B")
    elif money_before >= 10**6:
        money_divide = round(money_before / 10**6, 2)
        money_after = (str(money_divide) + " M")
    elif money_before >= 10**3:
        money_divide = round(money_before / 10**3, 2)
        money_after = (str(money_divide) + " K")
    else:
        return money_before
    return money_after