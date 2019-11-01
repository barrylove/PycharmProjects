import readConfig as readConfig
import readExcel as readExcel

readconfig = readConfig.ReadConfig()
readexcel = readExcel.ReadExcel()

class GeturlParams():  # 定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':' + readconfig.get_http('port') + readexcel.get_xls('TestCase_MerchantCancel.xlsx', 'Sheet1')[0][1]
        # logger.info('new_url'+new_url)
        return new_url


if __name__ == '__main__':  # 验证拼接后的正确性
    print(geturlParams().get_Url())