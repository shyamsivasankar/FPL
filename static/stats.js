var buttons = document.querySelectorAll('.player-stats')

async function fetchData() {
    try {
        const response = await fetch('/overall_data_fetch');
        const data = await response.json();
        var fpl_team = data['elements'];
        for (var i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener('click', function () {
                var card_data = document.querySelector('.player-details')
                    for (const j in fpl_team) {
                        if (fpl_team[j]['id'] == this.id) {
                            card_data.innerHTML = `<div class="player-basic-data">
                        <div class="player-image">
                            <img src="static/assets/Players/'` + fpl_team[j]['first_name']+` `+ fpl_team[j]['second_name']`+ '.png') " alt="" srcset="">
                        </div>
                        <div class="name">
                            <div class="first-name">` + fpl_team[j]['first_name'] + `</div>
                            <div class="second-name">` + fpl_team[j]['second_name'] + `</div>
                        </div>
                    </div>
                    <div class="player-basic-stats">
                        <div class="gw-select">
                            <div>
                                <div class="gw-header">Points</div>
                                <div class="gw-data">`+ fpl_team[j]['total_points'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">Minutes</div>
                                <div class="gw-data">` + fpl_team[j]['minutes'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">Goals</div>
                                <div class="gw-data">`+ fpl_team[j]['goals_scored'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">Assists</div>
                                <div class="gw-data">`+ fpl_team[j]['assists'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">Clean Sheets</div>
                                <div class="gw-data">`+ fpl_team[j]['clean_sheets'] + `</div>
                            </div>
                        </div>
                        <div class="card-line"></div>
                        <div class="gw-select">
                            <div>
                                <div class="gw-header">xG</div>
                                <div class="gw-data">`+ fpl_team[j]['expected_goals'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">xA</div>
                                <div class="gw-data">`+ fpl_team[j]['expected_assists'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">xGi</div>
                                <div class="gw-data">`+ fpl_team[j]['expected_goal_involvements'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">In</div>
                                <div class="gw-data">`+ fpl_team[j]['transfers_in_event'] + `</div>
                            </div>
                            <div>
                                <div class="gw-header">Out</div>
                                <div class="gw-data">`+ fpl_team[j]['transfers_out_event'] + `</div>
                            </div>
                        </div>
                    </div>`
                    console.log()
                        }
                    }
            })
        }

    } catch (error) {
        console.error('Error:', error);
        return "error"
    }
}

fetchData()