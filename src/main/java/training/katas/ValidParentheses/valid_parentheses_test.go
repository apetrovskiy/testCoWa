package ValidParentheses

import (
	// . "codewarrior/kata"
	// k "."
	"github.com/dailymotion/allure-go"
	"github.com/joho/godotenv"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	"log"
	"os"
	"testing"
)

// https://towardsdatascience.com/use-environment-variable-in-your-next-golang-project-39e17c3aaa66
// use godot package to load/read the .env file and
// return the value of the key
func goDotEnvVariable(key string) string {

	// load .env file
	err := godotenv.Load("../../../../../../variables.env")

	if err != nil {
		log.Fatal(err)
		log.Fatalf("Error loading .env file")
	}

	return os.Getenv(key)
}

var _ = Describe("Example Tests", func() {
	It("passes example tests", func() {
		Expect(ValidParentheses("()")).To(Equal(true))
		Expect(ValidParentheses(")")).To(Equal(false))
	})
})

func TestStepValidParentheses(t *testing.T) {
	goDotEnvVariable("ALLURE_RESULTS_PATH")
	allure.Test(t, allure.Action(func() {
		Expect(ValidParentheses("()")).To(Equal(true))
		Expect(ValidParentheses(")")).To(Equal(false))
		// wrong case
		// Expect(k.ValidParentheses("()")).To(Equal(false))
	}))
}
