from Modules.data_collection import fixtures,userteam,player,overall,gameweek,managerdata,managerHistory

async def team_data(managerid):
    manager_data = await managerdata(managerid=managerid)
    current_event = manager_data['current_event']
    user_data = await userteam(managerid=managerid,gameweek=str(current_event))
    overall_data =  await overall()
    week_details = await gameweek(str(current_event))
    mHist = await managerHistory(managerid=managerid)

    gw_points = [i['points'] for i in mHist['current']]
    x_axis = [str(i) for i in range(len(gw_points))]
    player_name =[]

    manager = { "first_name": manager_data['player_first_name'],
               "last_name" : manager_data['player_last_name'],
               "gw_points" : manager_data['summary_event_points'],
               "overall_points" : manager_data['summary_overall_points'],
               "gw_rank" : manager_data['summary_event_rank'],
               "overall_rank" : manager_data['summary_overall_rank'],
               "value" : float(user_data['entry_history']['value'])/10,
               "gw" : current_event}
    
    for i in user_data['picks']:
        for j in overall_data['elements']:
            if i['element'] == j['id']:
                temp = j 
                temp['is_captain'] = i['is_captain']
                player_name.append(temp)
                break

    avg_pts = []
    hst_pts = []
    for i in overall_data['events']:
        avg_pts.append(i['average_entry_score'])
        hst_pts.append(i['highest_score'])

    avg_pts = avg_pts[:current_event]
    hst_pts = hst_pts[:current_event]

    for i in player_name:
        for j in week_details['elements']:
            if i['id']==j['id']:
                i['points'] = (j['stats']['total_points'])
                break
        
        for j in overall_data['teams']:
            if i['team_code'] == j['code']:
                i['team_name'] = j['name']
                break
    
    # min_val = 100
    # differential_pick = {}
    # element_type_count = better_differntial_pick_count = 0
    # for i in player_name:
    #     if float(i['selected_by_percent']) < min_val:
    #         min_val = float(i['selected_by_percent'])
    #         differential_pick = i
    
    # for i in overall_data['elements']:
    #     if i['element_type'] == differential_pick['element_type']:
    #         element_type_data = await player(i['id'])
    #         if len(element_type_data['history']) > (current_event-1):
    #             element_type_count +=1
    #             if element_type_data['history'][current_event-1]['total_points'] > differential_pick['points']:
    #                 better_differntial_pick_count+=1
    # print(float((better_differntial_pick_count/element_type_count)*100))

    SUB = player_name[len(player_name)-4:]
    player_name= player_name[:len(player_name)-4]
    GK = [i for i in player_name if i['element_type'] == 1]
    DEF = [i for i in player_name if i['element_type'] == 2]
    MID = [i for i in player_name if i['element_type'] == 3]
    STR = [i for i in player_name if i['element_type'] == 4]
    fpl_team = [GK,DEF,MID,STR]

    return { 'fpl_team':fpl_team, 
            'SUB':SUB, 
            'Manager': manager, 
            'GWH': gw_points, 
            'x':x_axis,
            'avg_pts':avg_pts, 
            'hst_pts':hst_pts}