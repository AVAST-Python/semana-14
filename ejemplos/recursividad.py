
def yo_misma():
    print("Yo misma")
    yo_misma()

# yo_misma()


def yo_misma_2(n):
    if n == 0:
        return
    print("Yo misma")
    yo_misma_2(n-1)

yo_misma_2(3)
