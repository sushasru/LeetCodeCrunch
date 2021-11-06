class Solution:
    def myAtoi(self, str):
        num = 0 
        i = 0 
        sign = 0
        nomidspace = 0
        if len(str) > 0:
            if ord(str[0]) == 32 or ord(str[0]) == 43 or ord(str[0]) == 45 or (ord(str[0]) >= 48 and ord(str[0]) <= 57):
                #if str[0] == "-":
                    #sign = -1
                #else:
                    #sign = 1
                while i < len(str):
                    if str[i] == "+":
                        if sign == 0 and nomidspace == 0:
                            sign = 1
                            nomidspace = 1
                            i += 1
                        else:
                            if sign == 0:
                                sign = 1
                            return sign*num
                    elif str[i] == "-":
                        if sign == 0 and nomidspace == 0:
                            sign = -1
                            nomidspace = 1
                            i += 1
                        else:
                            if sign == 0:
                                sign = 1
                            return sign*num
                    elif str[i] == " ":
                        if nomidspace == 0:
                            i += 1
                        else:
                            if sign == 0:
                                sign = 1
                            return sign*num
                    elif str[i] == ".":
                        if sign == 0:
                            sign = 1
                        return sign*num
                    else:
                        if ord(str[i]) >= 48 and ord(str[i]) <= 57:
                            num = num * 10 + ord(str[i]) - ord('0')
                            nomidspace = 1
                            i += 1
                        else:
                            if sign == 0:
                                sign = 1
                            if num >= 2147483648 or num <= -2147483648 :
                                if sign == 1:
                                    return 2147483647
                                else:
                                    return -2147483648
                            else:
                                return sign*num
                            

                if sign == 0:
                    sign = 1
                if num >= 2147483648 or num <= -2147483648 :
                    if sign == 1:
                        return 2147483647
                    else:
                        return -2147483648
                else:
                    return sign*num
            else:
                return 0
        else:
            return 0
