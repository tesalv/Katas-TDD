from FizzBuzz.src import fizzbuzz

class TestFizzBuzz:
    def test_multiple_of_three(self):
        assert fizzbuzz.process(6)=="Fizz"
    
    def test_multiple_of_five(self):
        assert fizzbuzz.process(10)=="Buzz"
        
    def test_fizzbuzz(self):
        assert fizzbuzz.process(15)=="FizzBuzz"   
        assert fizzbuzz.process(30)=="FizzBuzz"  
        
    def test_regular_number(self):
        assert fizzbuzz.process(2)==2 
        assert fizzbuzz.process(11)==11 