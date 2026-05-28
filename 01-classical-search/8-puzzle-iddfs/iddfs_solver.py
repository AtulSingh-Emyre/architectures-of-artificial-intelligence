from AbstractEnvironment import I,S,BaseEnvironment

def depth_limited_search(game_env: BaseEnvironment, current_puzzle_sate: tuple[S,I],depth:int, path_set: set[tuple[S,I]]) -> tuple[bool,list]:
    # check if current state is goal state
    if(game_env.check_goal(current_puzzle_sate)):
        return (True, [current_puzzle_sate])
    # check if depth is 0 then return false
    elif depth == 0:
        return (False,[])
    else:
        path_set.add(current_puzzle_sate)
        # process next states
        next_puzzle_states = game_env.get_next_states(current_puzzle_sate)
        for next_puzzle_state in next_puzzle_states:
            if(path_set.__contains__(next_puzzle_state)):
                continue
            curr_branch = depth_limited_search(game_env,next_puzzle_state,depth-1, path_set)
            if curr_branch[0]:
                return (True, [current_puzzle_sate, *curr_branch[1]])
        path_set.remove(current_puzzle_sate)
        return (False,[])
    

def iddfs(game_env: BaseEnvironment) -> tuple[bool,list]:
    result_found: bool= False
    D = 0
    while True:
        # do depth limited search upto depth D
        active_branch_cache = set()
        current_result = depth_limited_search(game_env, current_puzzle_sate=game_env.get_initial_puzzle_state(),depth=D, path_set=active_branch_cache)
        if current_result[0]:
            return current_result
        D += 1
        if D == 15:
            print(f"We have searched upto Depth 25, please use a different search to avoid system crash")
            return (False,[])


