'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  ///
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000  # maximum price of item in the shop
MAX_QUANTITY = 100  # maximum quantity of an item in the shop
MAX_TOTAL = 1e6  # maximum total amount accepted for an order


def validorder(order):
    net = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            # sets a reasonable min & max value for the invoice amounts
            if item.amount > -1*MAX_ITEM_AMOUNT and item.amount < MAX_ITEM_AMOUNT:
                net += Decimal(str(item.amount))
        elif item.type == 'product':
            if item.quantity > 0 and item.quantity <= MAX_QUANTITY and item.amount > 0 and item.amount <= MAX_ITEM_AMOUNT:
                net -= Decimal(str(item.amount)) * item.quantity
            if net > MAX_TOTAL or net < -1*MAX_TOTAL:
                return ("Total amount exceeded")
        else:
            return ("Invalid item type: %s" % item.type)

    if net != 0:
        return ("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return ("Order ID: %s - Full payment received!" % order.id)