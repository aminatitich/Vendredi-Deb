text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at accumsan nisl, ac aliquet tellus. Sed maximus leo lacus, nec pulvinar purus maximus vel. Morbi sagittis suscipit risus, sed luctus metus bibendum vitae. Sed ac odio dignissim, efficitur ipsum eu, imperdiet ante. Sed eu lobortis nulla, placerat fermentum purus. Cras sollicitudin metus et imperdiet condimentum. Nulla a sapien sollicitudin nunc tincidunt interdum. Praesent elementum dolor id lacus lacinia, eu viverra arcu molestie. In nec neque ac ligula posuere gravida. Nulla maximus augue in consequat viverra. Integer euismod nibh a elit ullamcorper venenatis. In egestas, urna quis congue aliquam, risus lacus mollis nibh, sed venenatis dui lorem sed eros. Aliquam erat volutpat. Sed sagittis quam sed vestibulum ultricies. Cras sit amet efficitur nunc. Pellentesque mattis fermentum dui, finibus sagittis lacus sollicitudin quis. Praesent luctus pharetra nunc, vitae commodo ante laoreet sed. Sed eu lectus lectus. Nam luctus nisi quis porta fringilla. Quisque a tempus lectus. Cras at mauris tincidunt, volutpat eros vel, venenatis urna. Integer et tellus ut dui vulputate interdum ut id nunc."
vowel = "eioauy"
count = 0

i = 0
while i < len(text):
    if text[i] == vowel:
        count += 1

    i+=1

print(f"The number of vowels is: {count}.")