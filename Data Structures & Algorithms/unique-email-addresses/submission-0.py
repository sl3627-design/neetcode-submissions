class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = set()
        for email in emails:
            temp = email.split("@")
            domain = temp[1]
            if "+" in temp[0]:
                temp = temp[0].split("+")
            temp[0] = temp[0].replace(".", "")
            local = temp[0]
            d.add((local, domain))    
        
        return len(d)

