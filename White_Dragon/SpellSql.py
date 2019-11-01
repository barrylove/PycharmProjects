
def sumtotalamt(table, tradedata):
    sql = "SELECT sum(amt) FROM t_amon_order_"\
          + str(table) + " where date(trade_time)="\
          + "'" + tradedata + "'" + " and status = 1"
    return sql

#def sumpersonalamt(table):