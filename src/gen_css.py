import csslib

def main(o,out):
  writer = csslib.CssWriter(out)
  o.css(writer)
  writer.note()

import argparse,sys
parser = argparse.ArgumentParser()
parser.add_argument('type', choices=['sekki', 'sakugen', 'kyureki'])
parser.add_argument('--out',type=argparse.FileType(mode='w'),default=sys.stdout)

if __name__ == "__main__":
  args = parser.parse_args()
  match args.type:
    case 'sekki':
        import sekki as o
    case 'sakugen':
        import sakugen as o
    case 'kyureki':
        import kyureki as o
  
  main(o,args.out)