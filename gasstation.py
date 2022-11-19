from transport import Transport


class GasStation:
    @staticmethod
    def calculate_total_fuel(ls):
        total = 0

        for transport in ls:
            if isinstance(transport, Transport):
                total += transport.tank

        return total