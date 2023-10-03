import asyncio
from telegram import Bot

async def get_user_chat_id():
    # 봇 토큰을 설정합니다.
    telegram_bot_token = 'YOUR BOT TOKEN'

    # 텔레그램 봇 초기화
    bot = Bot(token=telegram_bot_token)

    # 최신 업데이트 가져오기
    updates = await bot.get_updates()
    
    if updates:
        # 최신 업데이트 중에서 가장 최근의 업데이트를 선택합니다.
        latest_update = updates[-1]

        # 사용자 정보 가져오기
        user_info = latest_update.message.from_user

        # 사용자의 채팅 ID 출력
        print(f"사용자의 채팅 ID: {user_info.id}")
    else:
        print("사용자가 봇에게 아직 메시지를 보내지 않았습니다.")

# 이벤트 루프를 생성하고 비동기 함수 호출
loop = asyncio.get_event_loop()
loop.run_until_complete(get_user_chat_id())
