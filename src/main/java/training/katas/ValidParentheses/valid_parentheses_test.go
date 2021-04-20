package kata_test

import (
	// . "codewarrior/kata"
	k "."
	"github.com/dailymotion/allure-go"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	"testing"
)

var _ = Describe("Example Tests", func() {
	It("passes example tests", func() {
		Expect(k.ValidParentheses("()")).To(Equal(true))
		Expect(k.ValidParentheses(")")).To(Equal(false))
	})
})

func TestStep(t *testing.T) {
	allure.Test(t, allure.Action(func() {
		Expect(k.ValidParentheses("()")).To(Equal(true))
		Expect(k.ValidParentheses(")")).To(Equal(false))
		// wrong case
		Expect(k.ValidParentheses("()")).To(Equal(false))
	}))
}
