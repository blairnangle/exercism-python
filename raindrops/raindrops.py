def convert(number):
    factor_to_sound = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }

    factors = list(filter(lambda factor: number % factor == 0, factor_to_sound.keys()))

    return str(number) if not factors else "".join(map(lambda factor: factor_to_sound[factor], factors))
