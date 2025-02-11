
        if a car is going past some car at an hour, it wont got past there, it will take the position of the car it is going past at the completion of the hour
        and then they both will travel the same speed as slower car.

        '''
        [10,9]
        [11,11]
        [1,1]

        speed = dist/time
        time = dist/speed
        prev_t = None
        for pos,vel in sorted(zip(position,speed))[::-1]:
        n = 0
            dist = target - pos
            time = dist / vel
            if not prev_t or time > prev_t:
                n += 1
                prev_t = time
        return n



        
        
