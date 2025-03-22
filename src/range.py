class Range:
    def map_range(self, x, in_min, in_max, out_min, out_max):
        val = (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

        if val > out_max:
            return out_max

        if val < out_min:
            return out_min

        return val

