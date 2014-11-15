from StringCalculator import StringCalculator
import argparse

class CommandLineStringCalculator(object):
    def parse_args(self):
        parser = argparse.ArgumentParser(description='StringCalculator (stringcal "12,4,5")')

        parser.add_argument('stringcal')
        parser.add_argument('string_sum', type=str)
        args = parser.parse_args()
        calc = StringCalculator()
        #result = cal.Add(operands=args.string_sum)
        result = calc.Add(args.string_sum)
        print(result)
        return result

if __name__ == '__main__':
  CommandLineStringCalculator().parse_args()