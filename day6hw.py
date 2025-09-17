total = 0
count = 0
blogviews = [150, 800, 2500, 600, 1200, 450, 3000]

for x in blogviews:
   if x>=1000:
      print(f"{x} Trending")
      count=count+1
   elif x<500:
      print(f"low traffic")
   elif x>500 and x<1000 :
      print(f"Average")
   total = total+x
   print(f"total={total}")
   print(f"count={count}")

      