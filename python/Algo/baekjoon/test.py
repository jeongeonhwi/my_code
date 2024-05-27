def replace_backslashes(input_string):
    """Replaces all single backslashes with double backslashes in a given string.

    Args:
        input_string (str): The string to modify.

    Returns:
        str: Modified string where all backslashes are doubled.
    """
    return input_string.replace('\\', '\\\\')


def decode_polyline(polyline_str):
    """Decodes a polyline that was encoded using the Google Maps algorithm.

    Args:
        polyline_str (str): Encoded polyline string.

    Returns:
        List of tuples where each tuple represents latitude and longitude.
    """
    index, lat, lng, coordinates = 0, 0, 0, []
    length = len(polyline_str)
    while index < length:
        for is_lat in [True, False]:  # True for latitude, False for longitude
            result, shift = 0, 0
            byte = 0x20
            while byte >= 0x20:
                if index >= length:  # Check if index exceeds the length of the string
                    return coordinates
                byte = ord(polyline_str[index]) - 63
                index += 1
                result |= (byte & 0x1f) << shift
                shift += 5
            if result & 1:
                result = ~result
            result >>= 1
            coord = result / 1e5
            if is_lat:  # This is for latitude
                lat += coord
            else:  # This is for longitude
                lng += coord
                coordinates.append([lat, lng])
    return coordinates

incodingPolyline = "{_zcF_offWRrCc@F}@LgGx@wEp@uC`@wAPi@Nc@Ro@b@OJ{@z@u@`Ao@lAi@zAkArEeBzGOj@o@bBy@vAi@n@i@l@o@f@o@`@a@Pe@Te@NODGBKBi@Rk@Ro@TSHUHm@TiBt@iBr@mBx@oBt@sBx@a@Lc@Ha@Hc@Bc@Bc@Ac@Ac@Ec@Ga@Ka@Ka@O_@Q_@U]U]WOQKKCCWWYa@KOIOUc@cBiEs@gBiB{E[y@O_@o@_Bm@{AKYIUUk@c@oA_@eAm@_Bm@aB_@aA_@_A[_Aa@eAa@iAc@kAWw@Ws@Uo@Qk@a@sAWy@K_@IYSu@Sy@Qs@Ss@Ia@I_@WcAmB{HW}@k@iBi@iBc@}Ae@aBWw@W{@o@oBk@iBSm@Qg@mA{Dc@qAa@oAs@}Bs@{BI[GMOc@a@iAk@}ACEQ_@GM_@WYE]EoCIcDIgDIgEKqBGoCG}BEuAEwAGc@Be@?cALi@RSHg@Xm@d@_@`@g@h@sAdBiAtAe@n@_@b@gAnASTe@`@_@\\i@`@{@l@UNgEhC}BtA}BvAcEdCwD~BuD~BeBfA_DnB{ClBoErCcCxAmCbBWPwAz@aAl@[N{@^[PYJk@Ts@PYHI?g@Hm@Js@DaAHI@_@@g@BmABuAB]@qBFmADy@DI?G@I?M@O@YFM@KBWHI@KDyAh@sBr@u@ZA?_@N_@PoBhAm@^cAt@wBfBwAhAiCnBkA|@gAx@aBnA}@t@{@p@QPSLa@\\uAdAq@f@m@d@k@b@mA|@c@ZOHwCrBwAx@oAh@WJi@V[R_@Zm@p@OPMPKN{@bB_@x@a@v@MVAFGLIj@SjAKrA?^?^?\\B`AD~BBzA?d@?l@EnAMbAWpCw@xIiApMOxAE\\Kv@CPQlA]zAOb@Wt@K\\Yl@_@z@]t@?@]f@_@h@KPs@r@ONw@n@SNo@^}@\\cAZeGf@gDXu@FQ@m@Bc@BaBLG?oAJyAHcEXeDRmGZC?iAJ_@DaARaATaATcARkAXiATkBb@eB\\{GtAcAP_@H[J_@N_@PWNWRQLUZQXMVGLWp@Of@GPEVEZC^CZAZAb@@\\@\\@RFd@F\\H`@Pb@r@nBZz@|@dCh@tAf@tATp@n@rBZlADVD\\BX?\\AXMtA_@jEAFOvCAj@?h@Dn@Bn@Bl@d@hFBf@B\\Fv@Bl@BbAC|AC^M~COhDOpBOpBA?"
non_escape_incodingPolyline = replace_backslashes(incodingPolyline)
decodingPolyline = decode_polyline(non_escape_incodingPolyline)
cnt = 0
for d in decodingPolyline:
    cnt += 1
    print(f'{d},')
print(cnt)