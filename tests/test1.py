from restpass.generator import Generator


CHECK = ["y", "eL", "7w1", "uwYO", "1HcR8", "jbGAV4", "KrOoKrg", "gBzUnbWk", "xkFn85JHz", "Sj4WS93zPX"]


if __name__ == "__main__":
    phrase = "Hello, World!"
    generator = Generator(phrase)
    generator.set_rules(digits=True, lowercase=True, uppercase=True)

    for i in range(1, 11):
        result = generator.generate(i)
        assert result == CHECK[i - 1]
        print(f"{i} - {result}")

    result = generator.generate(10)
    assert result == "Sj4WS93zPX"
    print("No salt:", result)  # No salt
    # Sj4WS93zPX

    generator.set_salt(b"Some salt")
    result = generator.generate(10)
    assert result == "0mIGvFXpoH"
    print("Some salt:", result)
    # 0mIGvFXpoH

    generator.set_salt(b"Some other salt")
    result = generator.generate(10)
    assert result == "iOkyf1VXOJ"
    print("Some other salt:", result)
    # iOkyf1VXOJ

    generator.set_salt(b"Some other salt", b"And a little more salt", b"Overwatch players")
    result = generator.generate(10)
    assert result == "IqCOWdHxgo"
    print("Some other salt, and a little more salt:", result)
    # IqCOWdHxgo
