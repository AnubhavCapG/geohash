def base32(number: int) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        number, remainder = divmod(number, 32)
        result = alphabet[remainder] + result
    return result


def main(precision: int = 10) -> None:
    user_lat, user_long = 12.973343525803152, 77.71789536074326
    lat_lower_bound, lat_upper_bound = -90, 90
    long_lower_bound, long_upper_bound = -180, 180
    lat_encoding, long_encoding = [], []
    for _ in range(precision):
        lat_mid = (lat_lower_bound + lat_upper_bound) / 2
        long_mid = (long_lower_bound + long_upper_bound) / 2
        if user_lat >= lat_mid:
            lat_encoding.append(1)
            lat_lower_bound = lat_mid
        else:
            lat_encoding.append(0)
            lat_upper_bound = lat_mid
        if user_long >= long_mid:
            long_encoding.append(1)
            long_lower_bound = long_mid
        else:
            long_encoding.append(0)
            long_upper_bound = long_mid
    alternating_encoding = [item for pair in zip(long_encoding, lat_encoding) for item in pair]
    built_chunks = [alternating_encoding[i:i+5] for i in range(0, len(alternating_encoding), 5)]
    connected_chunks = ["".join(map(str, chunk)) for chunk in built_chunks]
    geohash_binary_as_decimal = [int(chunk, 2) for chunk in connected_chunks]
    geohash_base32 = "".join(map(base32, geohash_binary_as_decimal))
    print(geohash_base32)
    

if __name__ == '__main__':
    main(15)