import math
import test_client

pi = math.pi

z_safety = 50

def main():

    x_list, y_list = test_client.order_classify('get_world_pos')
    
    pos_centri = (x_list[0],y_list[0],z_safety, 0, 0, 0)
    pos_suction = (x_list[1], y_list[1], z_safety, 0, 0, 0)
    pos_worktable = (x_list[2],y_list[2],z_safety, 0, 0, 0)
    pos_plate_sol = (x_list[3],y_list[3],z_safety, 0, 0, 0)
    pos_pipette = (x_list[4], y_list[4], z_safety, 0, 0, 0)
    pos_micro = (x_list[5], y_list[5], z_safety, 0, 0, 0)
    pos_incub = (x_list[6], y_list[6], z_safety, 0, 0, 0)

    #pos_centri = data.get_position("pos6", 0)
    #pos_suction = data.get_position("pos6", 1)
    #pos_worktable= data.get_position("pos6", 2)
    #pos_plate_sol = data.get_position("pos6", 3)
    #pos_pipette = data.get_position("pos6", 4)
    #pos_micro = data.get_position("pos6", 5)
    #pos_incub = data.get_position("pos6", 6)

    
if __name__ == '__main__':
    main()
