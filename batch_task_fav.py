# import schedule
# import time
# import datetime
from twitter_favorite_automated import favorite_automated


def batch_task1():
    print("batck task1 実行")
    favorite_automated(words1, favs1)

def batch_task2():
    print("batck task2 実行")
    favorite_automated(words2, favs2)


# ふぁぼ条件決定
words1 = ['共同浴場', '共同湯', '温泉マニア', '野湯']
words2 = ['かけ流し', 'かけながし', '掛け流し', '湯旅','湯めぐり', '湯巡り', '温泉めぐり', '温泉巡り', '温泉好き' , '温泉ファン', '温泉行きたい']
favs1 = 10
favs2 = 5

# 実行
batch_task1()
batch_task2()

# # 1分毎のjob実行を登録
# schedule.every(1).minutes.do(batch_task1)
# schedule.every(1).minutes.do(batch_task2)

# # 2時間毎のtask実行を登録
# schedule.every(2).hours.do(batch_task1)
# schedule.every(2).hours.do(batch_task2)


# # taskの実行監視、指定時間になったらtask関数を実行
# while True:
#     print(datetime.datetime.now())
#     schedule.run_pending()
#     time.sleep(1800)
#     #time.sleep(1)

# if __name__ == '__main__':
#     batch_task_twitter(words1, favs)
