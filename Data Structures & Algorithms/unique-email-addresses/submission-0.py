class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in range(len(emails)):
            fe = emails[i].split("@")[0].split("+")[0].replace(".", "") + "@" + emails[i].split("@")[1]

            s.add(fe)
        
        return len(s)


        