package kata // _test

import (
	// . "codewarrior/kata"
	"github.com/dailymotion/allure-go"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	"testing"
)

var _ = Describe("Example Tests", func() {
	It("passes example tests", func() {
		Expect(ValidParentheses("()")).To(Equal(true))
		Expect(ValidParentheses(")")).To(Equal(false))
	})
})

func TestStep(t *testing.T) {
	allure.Test(t, allure.Action(func() {
		Expect(ValidParentheses("()")).To(Equal(true))
		Expect(ValidParentheses(")")).To(Equal(false))
	}))
}
