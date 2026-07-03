class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # d = set()
        # for email in emails:
        #     temp = email.split("@")
        #     domain = temp[1]
        #     if "+" in temp[0]:
        #         temp = temp[0].split("+")
        #     temp[0] = temp[0].replace(".", "")
        #     local = temp[0]
        #     d.add((local, domain))    
        
        # return len(d)

        unique = set()

        for e in emails:
            # local, domain = e.split("@")
            # local = local.split("+")[0]
            # local = local.replace(".", "")
            # unique.add((local, domain))

            i, local = 0, ""
            while e[i] not in ["@", "+"]: 
                if e[i] != ".":
                    local += e[i]
                i += 1
            
            while e[i] != "@":
                i += 1
            domain = e[i+1:]

            unique.add((local, domain))
        return len(unique)

        
