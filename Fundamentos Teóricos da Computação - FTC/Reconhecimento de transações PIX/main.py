import re

class Invalid(Exception):     
      def __init__(self, *args: object) -> None:
            super().__init__(*args)
            
class Validation:

      def validate_cpf(word):   
            search = re.search('(\d{3}\.\d{3}\.\d{3}-\d{2})', word) 

            if  search: 
                  out = search.group(1)
                  if Certification.certify_cpf(out):
                        word = re.sub("(\d{3}\.\d{3}\.\d{3}-\d{2})", "", word)

            return word


      def validate_cnpj(word): 
            search = re.search("([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})", word) 

            if  search:
                  slice = search.group(1)
                  if Certification.certify_cnpj(slice):
                        word = re.sub("([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})","", word)

            return word
            
                  
      def validate_email(word) -> bool:   
            if re.search("^\D+\w*@\w+(.|\w)+", word): 
                 word = re.sub("^\D+\w*@\w+(.|\w)+", "", word)
                 
            return word

      def validate_PhoneNumber(word) -> bool:
            if re.search("\+55\(\d{2}\)\d{4}-\d{4}", word): 
                  word = re.sub("\+55\(\d{2}\)\d{4}-\d{4}", "", word)
            return word

      def validate_quickKey(word) -> bool:  
            if re.search("[0-9A-F]{2}.[0-9A-F]{2}.[0-9A-F]{2}.[0-9A-F]{2}", word): 
                  word = re.sub("[0-9A-F]{2}.[0-9A-F]{2}.[0-9A-F]{2}.[0-9A-F]{2}", "", word)
            
            return word

      def validate_separator(word) -> bool:
                  if re.search(r'=+',  word): 
                        if len(separator) == 10:
                              return True
                  return False
            
      
      def validate_timestampDate(date) ->bool:
            if re.search("([0-3][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d+", date):
                  date = re.sub("([0-3][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d+", "", date)
            return date

      def validate_transactionAmount(word) -> bool:
            if re.search("R\$ ?\d{1,3}(\.\d{3})*,\d{2}", word): 
                  word = re.sub("R\$ ?\d{1,3}(\.\d{3})*,\d{2}","", word )
            return word
      
      def validate_timestampHHNN(word) -> bool:
            if re.search("([01]?[0-9]|2[0-3]):([0-5][0-9])", word):
                  word = re.sub("([01]?[0-9]|2[0-3]):([0-5][0-9])", "", word)
            return word

      def validate_securityCode(word) -> bool:  
            if re.search("[a-zA-Z$@%(*0-9]{12}", word):
                  word = re.sub("[a-zA-Z$@%(*0-9]{12}", "", word)
            return word

class Certification:

      def certify_cpf(cpf:str):
            try:
                  nums_list = []
                  for number in cpf:
                        if number.isdigit(): nums_list.append(int(number))

                  if len(nums_list) != 11 or len(set(nums_list)) == 1: 
                        return False
                        
                  sum_of_products = sum(a * b for a, b in zip(nums_list[0:9], range(10, 1, -1)))
                  expected_digit = (sum_of_products * 10 % 11) % 10
                  if nums_list[9] != expected_digit: 
                        return False

                  sum_of_products = sum(a * b for a, b in zip(nums_list[0:10], range(11, 1, -1)))
                  expected_digit = (sum_of_products * 10 % 11) % 10
                  if nums_list[10] != expected_digit: 
                        return False

                  return True

            except:
                  raise Invalid("False")

      def certify_cnpj(cnpj:str):
            try:
                  cnpj = "".join(re.findall('\d', str(cnpj)))
                  
                  if len(cnpj) < 14:
                        return False
                  
                  inteiros = list(map(int, cnpj))
                  novo = inteiros[:12]

                  prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                  while len(novo) < 14:
                        r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
                        if r > 1:
                              f = 11 - r
                        else: 
                              f = 0
                        novo.append(f)
                        prod.insert(0, 6)

                  if novo == inteiros: 
                        return True
            except:
                  raise Invalid("False")
            
def keys_validation(keys:list):
      states = []

      keys= Validation.validate_cpf(keys)
      states.append((Validation.validate_cnpj(keys)))
      states.append((Validation.validate_email(keys)))
      states.append((Validation.validate_PhoneNumber(keys)))
      states.append((Validation.validate_quickKey(keys)))

      return len(keys) == 0
     
def separator_validation(separator:list):
      try:
            if Validation.validate_separator(separator):
                  return True
            else:
                  return False
      except:
            raise Invalid("False")

def transfer_validation(transfer:list):
      states = []
      states.append((Validation.validate_cpf(transfer)))
      states.append((Validation.validate_cnpj(transfer)))
      states.append((Validation.validate_email(transfer)))
      states.append((Validation.validate_PhoneNumber(transfer)))
      states.append((Validation.validate_quickKey(transfer)))
      states.append((Validation.validate_transactionAmount(transfer)))
      states.append((Validation.validate_timestampHHNN(transfer)))
      states.append((Validation.validate_timestampDate(transfer)))    
      states.append((Validation.validate_securityCode(transfer)))

      return len(transfer) == 0

if __name__ == "__main__":
      key_list, separator, transfer = [], [], []
     
      while True:
            try:
                  linha = input()
                  key_list.append(linha)

                  if linha == "="*10:
                        separator.append(linha)
                        continue
                  else:
                        transfer.append(linha)
            except EOFError:
                  break

if keys_validation(key_list) and separator_validation(separator) and transfer_validation(transfer):
      print("True")
else:
      print("False")     
