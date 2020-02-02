import requests
import sys, time, os
import logging
import re


# 已下载的个数

def get_page(url):
    response = requests.get(url)
    return response


def download(name):
    file_name = str(name)
    # print(file_name)
    # file_name = "1QIyv1Kg3296" + str_name + '.ts'  # 【根据url修改】
    uri = url.rsplit("/", 1)[0];
    newUrl = uri + "/" + file_name
    # print(newUrl)
    try:
        res = requests.get(url=newUrl, timeout=30)
        content = res.content

        with open(tsDict % (r'\ts'+file_name), 'wb')as f:
            f.write(content)
            # print(file_name + '\x1b[1;30;42m 下载成功 \033[0m')
            # print(file_name + '下载完成，' + '已下载' + ' %s %% %s' % (round(downLength / tsLength,2), '>' * downLength))  # 【假的进度条，能看个大概，根据url修改】
    except Exception as e:
        # 报错提示
        print(file_name + '\x1b[1;30;41m 下载失败 \033[0m')
        print(e)
        # name = re.findall('1QIyv1Kg3296(\d+).ts', file_name)[0]  # 【根据url修改】
        print(name + ' 下载失败')

        # 记录日志
        my_log = logging.getLogger('lo')
        my_log.setLevel(logging.DEBUG)
        file = logging.FileHandler('error.log', encoding='utf-8')
        file.setLevel(logging.ERROR)
        my_log_fmt = logging.Formatter('%(asctime)s-%(levelname)s:%(message)s')
        file.setFormatter(my_log_fmt)
        my_log.addHandler(file)
        my_log.error(file_name + ' 下载失败 ')
        my_log.error(e)

        # 重新下载
        download(name)  # 如果报错，递归执行一遍


def changeType():
    files = os.listdir(tsDict % '')

    tmp = []
    for file in files[0:tsLength]:
        tmp.append(file.replace("\n", ""))
        # 合并ts文件
    os.chdir(tsDict % '')
    shell_str = '+'.join(tmp)
    # print(shell_str)
    shell_str = 'copy /b ' + shell_str + ' ' + mp4Name + '.mp4'

    os.system(shell_str)
    print(shell_str)


from concurrent.futures import ThreadPoolExecutor  # 线程池

p = ThreadPoolExecutor(10)
# 1
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/026b23f313014b71b01846693932ac67/tranbox/026b23f313014b71b01846693932ac67_g4Z81.m3u8?aliyun_uuid=e385a302ec794ec2b3451b77b13794df'
# 2
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/3adab29d4b624aa1ba19ec9879610105/tranbox/3adab29d4b624aa1ba19ec9879610105_EGDK0.m3u8?aliyun_uuid=1cd3f3d1e2a24cc6ad43d7ee27d86edf'
# 3
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/015f13ff8a2f4fdab21bfca2c37ef480/tranbox/015f13ff8a2f4fdab21bfca2c37ef480_P6Tth.m3u8?aliyun_uuid=d406f704e9204c60b1cea9ff79caec94'
# 4
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/d3eb9fd533bd4eff94101c9b6e30a04a/tranbox/d3eb9fd533bd4eff94101c9b6e30a04a_treD0.m3u8?aliyun_uuid=8e30180720b3462e996255c5b6d99e82'
# 5
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/2fd1b599671f43438a8c37857f3912a4/tranbox/2fd1b599671f43438a8c37857f3912a4_tAHRw.m3u8?aliyun_uuid=19bf298e08984f3eb4ee129e7e8377cf'
# 6
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/e4e96aaadc724772a052d0e4aee0cea3/tranbox/e4e96aaadc724772a052d0e4aee0cea3_xzkBe.m3u8?aliyun_uuid=340c6075226e4b0092edcf63929ff9a6'
# 7
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/0fe2615f0bae45a998835df6fea42f09/tranbox/0fe2615f0bae45a998835df6fea42f09_QWRiC.m3u8?aliyun_uuid=4c9d2f0426a94b74bd6c3f1455e9664f'
# 8
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/e4e96aaadc724772a052d0e4aee0cea3/tranbox/e4e96aaadc724772a052d0e4aee0cea3_xzkBe.m3u8?aliyun_uuid=539551a10b5c45149ace5270bd2494a7'
# 8
url = f'http://cdn-host.media.yunxi.tv/recordM3u8/248df5aea3b447728620b59258996c13/tranbox/248df5aea3b447728620b59258996c13_Iim7z.m3u8?aliyun_uuid=2e2d1a4c6baf48a6923fcd4ad0c78ce3'
# 9
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/0fe2615f0bae45a998835df6fea42f09/tranbox/0fe2615f0bae45a998835df6fea42f09_QWRiC.m3u8?aliyun_uuid=ba4f774119fb46e5b8de126ca055916b'
# 10
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/7cb6303d3b2e4c9c8dec1d56df76ab47/tranbox/7cb6303d3b2e4c9c8dec1d56df76ab47_tKmLr.m3u8?aliyun_uuid=a8ebb10e7de14c2ab257efe14e031c9a'
# 11
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/afa3eaf1859745e094cab0104e6c021d/tranbox/afa3eaf1859745e094cab0104e6c021d_RJLRp.m3u8?aliyun_uuid=2429032119144624a65107d6a2637879'
# 12
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/147b64a356d34bb59f71124b37991401/tranbox/147b64a356d34bb59f71124b37991401_HNI9K.m3u8?aliyun_uuid=abc8644b83ff433189e29ce240ba7b02'
# 13
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/83d24a3be5eb4c30a00a2534cbe824fe/tranbox/83d24a3be5eb4c30a00a2534cbe824fe_3Lytl.m3u8?aliyun_uuid=2c22c21dcb334f5b9faf5ae629b8c8b0'

# 发送请求
response = get_page(url)
# print(respone)
# # 返回响应状态码
# print(response.status_code)
# 返回响应文本
# print(response.text)
list1 = response.text.split("\n");
list2 = [];
# 下载视频的目录
dict = r'G:\vedio\pmp\vedio8\%s';
tsDict = r'G:\vedio\pmp\vedio8\tmp\%s';
# 转成成MP4格式的视频名称
mp4Name = "第八章：项目质量管理"
for x in list1:
    if '.ts' in x:
        list2.append(x);

print('将要下载的文件个数：%s' % len(list2))
tsLength = len(list2);
downLength = 0

if not os.path.exists(tsDict % ''):
    os.makedirs(tsDict % '')

for name in list2:  # 【根据url修改】
    downLength += 1
    p.submit(download, name)
    jindu = '>' * (downLength // 2) + ' ' * ((tsLength - downLength) // 2)
    sys.stdout.write('\r' + jindu + '[%s%%]' % (round(downLength / tsLength * 100, 2)))
    time.sleep(0.1)
time.sleep(5)
#转换成mp4
changeType()

# str = str.zfill(5) 左边补零操作

# 功能：失败提示，失败重试，失败记录日志，线程池提高并发，超时重试。
# 打开cmd，切进目录，执行copy /b *.ts video.ts合并速度超快。
# 打开cmd，切进目录，执行copy /b *.ts video.mp4合并速度超快。
