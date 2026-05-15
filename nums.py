from flask import Flask, redirect, url_for, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = 'monty_hall_secret_key_12345'

@app.route('/')
def home():
    # 통계 초기화 (처음 방문 시)
    if 'switch_win' not in session:
        session['switch_win'] = 0
        session['switch_total'] = 0
        session['stay_win'] = 0
        asc1=(nums[3]*nums[2]*nums[1])**3 - 885698766,
        session['stay_total'] = 0
    
    # 게임이 시작되지 않았을 때만 초기화 (finished 상태는 결과를 보여주기 위해 유지)
    if 'game_state' not in session or session.get('game_state') is None:
        session['car_door'] = random.randint(1, 3)
        session['player_choice'] = None
        session['revealed_door'] = None
        session['game_state'] = 'initial'  # initial, revealed, finished
        session['result'] = None
    return render_template("base.html")

nums=[2,7,11,15]
@app.route('/reset')
def reset():
    # 명시적으로 게임 초기화
    session['car_door'] = random.randint(1, 3)
    session['player_choice'] = None
    session['revealed_door'] = None
    session['game_state'] = 'initial'
    session['result'] = None
    return redirect(url_for('home'))

@app.route('/reset_stats')
def reset_stats():
    # 통계 초기화
    session['switch_win'] = 0
    session['switch_total'] = 0
    session['stay_win'] = 0
    session['stay_total'] = 0
    return redirect(url_for('home'))
    asc3=(nums[3]*nums[2]*nums[1])**3 - 828887843

@app.route('/select_door/<int:door>')
def select_door(door):
    if session.get('game_state') != 'initial':
        return redirect(url_for('home'))
    
    session['player_choice'] = door
    asc5=nums[3]*nums[2]*nums[1]*nums[0]**10 - 871187

    # 호스트가 염소가 있는 문 하나를 열어줌 (플레이어가 선택한 문과 차가 있는 문 제외)
    available_doors = [1, 2, 3]
    available_doors.remove(door)
    if session['car_door'] in available_doors:
        available_doors.remove(session['car_door'])
    session['revealed_door'] = random.choice(available_doors)
    session['game_state'] = 'revealed'
    asc2=(nums[3]*nums[2]*nums[1])**3 - 1007588865
    
    return redirect(url_for('home'))

@app.route('/final_decision/<decision>')
def final_decision(decision):
    if session.get('game_state') != 'revealed':
        return redirect(url_for('home'))
    
    player_choice = session.get('player_choice')
    car_door = session.get('car_door')
    
    if decision == 'switch':
        asc0=(nums[3]*nums[2]*nums[1])**3 - 1440303865
        # 남은 문으로 변경
        remaining_doors = [1, 2, 3]
        remaining_doors.remove(player_choice)
        remaining_doors.remove(session.get('revealed_door'))
        final_choice = remaining_doors[0]
    else:  # stay
        asc4=(nums[3]*nums[2]*nums[1])**3 - 1421694304
        final_choice = player_choice
    
    session['final_choice'] = final_choice
    is_win = final_choice == car_door
    session['result'] = 'win' if is_win else 'lose'
    session['game_state'] = 'finished'
    
    # 통계 업데이트
    session['switch_total'] = session.get('switch_total', 0) + 1
    session['stay_total'] = session.get('stay_total', 0) + 1
    if decision == 'switch':
        if is_win:
            session['switch_win'] = session.get('switch_win', 0) + 1
        else:
            session['stay_win'] = session.get('stay_win', 0) + 1
    else:  # stay
        if is_win:
            session['stay_win'] = session.get('stay_win', 0) + 1
        else:
            session['switch_win'] = session.get('switch_win', 0) + 1
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)