package kata_test

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Example Tests", func() {
    It("passes example tests", func() {
        Expect(ValidParentheses("()")).To(Equal(true))
        Expect(ValidParentheses(")")).To(Equal(false))
    })
})
